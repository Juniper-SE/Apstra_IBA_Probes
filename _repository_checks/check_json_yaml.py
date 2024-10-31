"""
Enhanced validation for JSON and YAML files with detailed error reporting.

This script provides detailed validation of JSON and YAML files, including:
- Line number identification for errors
- Context of where errors occur
- Detailed error messages with file locations
- Support for both JSON and YAML formats
"""

# Standard library imports
import json  # JSON parsing and validation
import yaml  # YAML parsing and validation
import os    # File and directory operations
from common import setup_logging  # Import shared logging configuration
from typing import Dict, List, Tuple  # Type hints for better code documentation

class JsonValidationError:
    """
    Custom error class to store and format validation errors.
    
    This class standardizes error reporting across both JSON and YAML validation,
    providing consistent error messages with line numbers and context.
    
    Attributes:
        file_path (str): Path to the file containing the error
        error_msg (str): Description of the error
        line_number (int, optional): Line number where the error occurred
    """
    def __init__(self, file_path: str, error_msg: str, line_number: int = None):
        self.file_path = file_path
        self.error_msg = error_msg
        self.line_number = line_number
        
    def __str__(self):
        """
        Format the error message with file name, line number (if available), and error details.
        
        Example outputs:
            "config.json at line 15: Expecting ',' delimiter"
            "config.yaml: Invalid YAML syntax"
        """
        location = f" at line {self.line_number}" if self.line_number is not None else ""
        return f"{os.path.basename(self.file_path)}{location}: {self.error_msg}"

def get_json_line_number(json_str: str, pos: int) -> int:
    """
    Calculate the line number in a JSON string based on character position.
    
    Args:
        json_str (str): The complete JSON content
        pos (int): Character position where the error occurred
        
    Returns:
        int: Line number (1-based) where the error occurred
        
    Note:
        This function counts newlines up to the error position and adds 1
        because line numbers are 1-based, not 0-based.
    """
    return json_str.count('\n', 0, pos) + 1

def validate_json_file(file_path: str) -> List[JsonValidationError]:
    """
    Validate a single JSON file and provide detailed error information.
    
    Args:
        file_path (str): Path to the JSON file to validate
        
    Returns:
        List[JsonValidationError]: List of validation errors found
                                  Empty list if file is valid
    
    This function:
    1. Reads the file content
    2. Attempts to parse it as JSON
    3. If errors occur, captures:
       - Line number
       - Context (the problematic line)
       - Detailed error message
    """
    errors = []
    try:
        # Attempt to read the file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            try:
                # Attempt to parse JSON
                json.loads(content)
            except json.JSONDecodeError as e:
                # JSON parsing failed - gather error details
                line_number = get_json_line_number(content, e.pos)
                
                # Get the line containing the error for context
                lines = content.split('\n')
                context = lines[line_number - 1] if line_number <= len(lines) else ""
                
                # Create detailed error message with context
                error_msg = f"{str(e)}\nContext: {context.strip()}"
                errors.append(JsonValidationError(file_path, error_msg, line_number))
    except Exception as e:
        # File reading failed
        errors.append(JsonValidationError(file_path, f"Failed to read file: {str(e)}"))
    
    return errors

def validate_json_yaml_files(release_path: str) -> Dict[str, List[JsonValidationError]]:
    """
    Validate all JSON and YAML files in a release directory.
    
    Args:
        release_path (str): Path to the release directory to check
        
    Returns:
        Dict containing two lists:
        - 'invalid_json': List of JSON validation errors
        - 'invalid_yaml': List of YAML validation errors
        
    This function:
    1. Recursively finds all JSON and YAML files
    2. Validates each file's syntax
    3. Collects and categorizes any errors found
    """
    logger = setup_logging()
    issues = {
        'invalid_json': [],
        'invalid_yaml': []
    }
    
    # Walk through all subdirectories
    for root, _, files in os.walk(release_path):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Validate JSON files
            if file.endswith('.json'):
                errors = validate_json_file(file_path)
                if errors:
                    issues['invalid_json'].extend(errors)
            
            # Validate YAML files
            elif file.endswith(('.yaml', '.yml')):
                try:
                    with open(file_path) as f:
                        yaml.safe_load(f)
                except yaml.YAMLError as e:
                    error_msg = f"YAML Error: {str(e)}"
                    issues['invalid_yaml'].append(JsonValidationError(file_path, error_msg))
    
    return issues

# Script entry point - allows running this file directly for testing
if __name__ == "__main__":
    logger = setup_logging()
    issues = validate_json_yaml_files(".")
    
    if any(issues.values()):
        print("\nJSON/YAML Issues Found:")
        
        # Report JSON validation errors
        if issues['invalid_json']:
            print("\n📊 Invalid JSON files:")
            for error in issues['invalid_json']:
                print(f"❌  {error}")
        
        # Report YAML validation errors        
        if issues['invalid_yaml']:
            print("\n📝 Invalid YAML files:")
            for error in issues['invalid_yaml']:
                print(f"❌  {error}")
        exit(1)
    
    print("✅ No JSON/YAML issues found.")
    exit(0)