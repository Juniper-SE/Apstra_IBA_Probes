"""
Enhanced validation for JSON and YAML files with detailed error reporting.
"""
import json
import yaml
import os
from common import setup_logging
from typing import Dict, List, Tuple

class JsonValidationError:
    def __init__(self, file_path: str, error_msg: str, line_number: int = None):
        self.file_path = file_path
        self.error_msg = error_msg
        self.line_number = line_number
        
    def __str__(self):
        location = f" at line {self.line_number}" if self.line_number is not None else ""
        return f"{os.path.basename(self.file_path)}{location}: {self.error_msg}"

def get_json_line_number(json_str: str, pos: int) -> int:
    """
    Find the line number in a JSON string based on position
    """
    return json_str.count('\n', 0, pos) + 1

def validate_json_file(file_path: str) -> List[JsonValidationError]:
    """
    Validate a single JSON file with detailed error reporting
    """
    errors = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            try:
                json.loads(content)
            except json.JSONDecodeError as e:
                # Get line number from error position
                line_number = get_json_line_number(content, e.pos)
                
                # Get context of the error
                lines = content.split('\n')
                context = lines[line_number - 1] if line_number <= len(lines) else ""
                
                # Create detailed error message
                error_msg = f"{str(e)}\nContext: {context.strip()}"
                errors.append(JsonValidationError(file_path, error_msg, line_number))
    except Exception as e:
        errors.append(JsonValidationError(file_path, f"Failed to read file: {str(e)}"))
    
    return errors

def validate_json_yaml_files(release_path: str) -> Dict[str, List[JsonValidationError]]:
    """
    Check all JSON and YAML files in a release with detailed error reporting
    """
    logger = setup_logging()
    issues = {
        'invalid_json': [],
        'invalid_yaml': []
    }
    
    for root, _, files in os.walk(release_path):
        for file in files:
            file_path = os.path.join(root, file)
            
            if file.endswith('.json'):
                errors = validate_json_file(file_path)
                if errors:
                    issues['invalid_json'].extend(errors)
            
            elif file.endswith(('.yaml', '.yml')):
                try:
                    with open(file_path) as f:
                        yaml.safe_load(f)
                except yaml.YAMLError as e:
                    error_msg = f"YAML Error: {str(e)}"
                    issues['invalid_yaml'].append(JsonValidationError(file_path, error_msg))
    
    return issues

if __name__ == "__main__":
    logger = setup_logging()
    issues = validate_json_yaml_files(".")
    
    if any(issues.values()):
        print("\nJSON/YAML Issues Found:")
        
        if issues['invalid_json']:
            print("\n📊 Invalid JSON files:")
            for error in issues['invalid_json']:
                print(f"❌  {error}")
                
        if issues['invalid_yaml']:
            print("\n📝 Invalid YAML files:")
            for error in issues['invalid_yaml']:
                print(f"❌  {error}")
        exit(1)
        
    print("✅ No JSON/YAML issues found.")
    exit(0)
