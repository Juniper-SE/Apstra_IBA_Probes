"""
Enhanced reporting functionality with improved visual formatting.
"""
import os
from typing import Dict, List, Any
from datetime import datetime

# ANSI color codes for terminal output
class Colors:
    HEADER = '\033[95m'  # Pink
    OKBLUE = '\033[94m'  # Blue
    OKGREEN = '\033[92m' # Green
    WARNING = '\033[93m' # Yellow
    FAIL = '\033[91m'    # Red
    ENDC = '\033[0m'     # Reset
    BOLD = '\033[1m'     # Bold

# Emoji indicators for different status types
EMOJI = {
    'success': '✅',
    'error': '❌',
    'warning': '⚠️',
    'info': 'ℹ️',
    'folder': '📁',
    'file': '📄',
    'image': '🖼️',
    'json': '📊',
    'yaml': '📝',
    'check': '🔍'
}

def create_section_header(title: str) -> str:
    """Create a formatted section header with consistent styling"""
    return f"\n{Colors.BOLD}{Colors.HEADER}{'='*60}{Colors.ENDC}\n{Colors.BOLD}{title}{Colors.ENDC}\n{Colors.BOLD}{Colors.HEADER}{'='*60}{Colors.ENDC}\n"

def create_subsection_header(title: str) -> str:
    """Create a formatted subsection header"""
    return f"\n{Colors.BOLD}{Colors.OKBLUE}{'-'*40}\n{title}\n{'-'*40}{Colors.ENDC}\n"

def format_error(message: str) -> str:
    """Format error messages in red with error emoji"""
    return f"{Colors.FAIL}{EMOJI['error']} {message}{Colors.ENDC}"

def format_warning(message: str) -> str:
    """Format warning messages in yellow with warning emoji"""
    return f"{Colors.WARNING}{EMOJI['warning']} {message}{Colors.ENDC}"

def format_success(message: str) -> str:
    """Format success messages in green with success emoji"""
    return f"{Colors.OKGREEN}{EMOJI['success']} {message}{Colors.ENDC}"

def format_info(message: str) -> str:
    """Format informational messages in blue with info emoji"""
    return f"{Colors.OKBLUE}{EMOJI['info']} {message}{Colors.ENDC}"

def format_release_header(release: str) -> str:
    """Format a release section header"""
    return create_section_header(f"📦 Checking Release: {release}")

def format_component_header(component: str) -> str:
    """Format a component section header"""
    return create_subsection_header(f"Checking Component: {component}")

def format_structure_issues_content(issues: Dict[str, List[str]]) -> str:
    """Format just the structure issues content"""
    lines = []
    for component, component_issues in issues.items():
        lines.append(f"\n{EMOJI['folder']} {Colors.BOLD}{component}:{Colors.ENDC}")
        for issue in component_issues:
            lines.append(format_error(f"    {issue}"))
    return "\n".join(lines)

def format_json_yaml_issues_content(issues: Dict[str, List[str]]) -> str:
    """Format just the JSON/YAML issues content"""
    lines = []
    if issues['invalid_json']:
        lines.append(f"\n{EMOJI['json']} {Colors.BOLD}Invalid JSON files:{Colors.ENDC}")
        for error in issues['invalid_json']:
            lines.append(format_error(f"    {str(error)}"))
            
    if issues['invalid_yaml']:
        lines.append(f"\n{EMOJI['yaml']} {Colors.BOLD}Invalid YAML files:{Colors.ENDC}")
        for error in issues['invalid_yaml']:
            lines.append(format_error(f"    {str(error)}"))
    return "\n".join(lines)

def format_image_issues_content(issues: Dict[str, List[str]]) -> str:
    """Format just the image issues content"""
    lines = []
    if issues['broken_links']:
        lines.append(f"{EMOJI['image']} {Colors.BOLD}Broken Links:{Colors.ENDC}")
        for link in issues['broken_links']:
            lines.append(format_error(f"    {link}"))
            
    if issues['unused_images']:
        if issues['broken_links']:
            lines.append("")
        lines.append(f"{EMOJI['image']} {Colors.BOLD}Unused Images:{Colors.ENDC}")
        for image in issues['unused_images']:
            lines.append(format_warning(f"    {image}"))
    return "\n".join(lines)

def format_full_report(release: str, results: Dict[str, Any]) -> str:
    """Generate a full report with clear visual separation between sections"""
    sections = []
    
    # Release Header
    sections.append(format_release_header(release))
    
    # Structure Section
    sections.append(create_section_header("Structure Validation"))
    structure_issues = results.get('structure_issues', {})
    if structure_issues:
        sections.append(format_structure_issues_content(structure_issues))
    else:
        sections.append(format_success("No structure issues found"))
        
    # JSON/YAML Section
    sections.append(create_section_header("JSON/YAML Validation"))
    json_yaml_issues = results.get('json_yaml_issues', {})
    if any(json_yaml_issues.values()):
        sections.append(format_json_yaml_issues_content(json_yaml_issues))
    else:
        sections.append(format_success("No JSON/YAML issues found"))
    
    # Image Section
    sections.append(create_section_header("Image Validation"))
    image_issues = results.get('image_issues', {})
    if image_issues:
        for component, issues in image_issues.items():
            sections.append(format_component_header(component))
            if any(issues.values()):
                sections.append(format_image_issues_content(issues))
            else:
                sections.append(format_success(f"No image issues found in {component}"))
    
    return "\n".join(sections)

def generate_summary_tally(all_results: Dict[str, Dict[str, Any]]) -> str:
    """Generate a summary tally with improved visual formatting"""
    total_issues = {
        'structure': 0,
        'json': 0,
        'yaml': 0,
        'broken_links': 0,
        'unused_images': 0,
        'components_checked': 0,
        'releases_checked': len(all_results)
    }
    
    for release_results in all_results.values():
        # Count structure issues
        structure_issues = release_results.get('structure_issues', {})
        total_issues['structure'] += sum(len(issues) for issues in structure_issues.values())
        
        # Count JSON/YAML issues
        json_yaml_issues = release_results.get('json_yaml_issues', {})
        total_issues['json'] += len(json_yaml_issues.get('invalid_json', []))
        total_issues['yaml'] += len(json_yaml_issues.get('invalid_yaml', []))
        
        # Count image issues
        image_issues = release_results.get('image_issues', {})
        total_issues['components_checked'] += len(image_issues)
        for component_issues in image_issues.values():
            total_issues['broken_links'] += len(component_issues.get('broken_links', []))
            total_issues['unused_images'] += len(component_issues.get('unused_images', []))

    lines = [
        create_section_header("Final Summary"),
        f"{EMOJI['info']} {Colors.BOLD}Scope:{Colors.ENDC}",
        f"    Releases checked: {total_issues['releases_checked']}",
        f"    Components checked: {total_issues['components_checked']}",
        "",
        f"{EMOJI['error']} {Colors.BOLD}Errors Found:{Colors.ENDC}",
        f"    Structure issues: {total_issues['structure']}",
        f"    Invalid JSON files: {total_issues['json']}",
        f"    Invalid YAML files: {total_issues['yaml']}",
        f"    Broken image links: {total_issues['broken_links']}",
        "",
        f"{EMOJI['warning']} {Colors.BOLD}Warnings Found:{Colors.ENDC}",
        f"    Unused images: {total_issues['unused_images']}",
        ""
    ]

    total_errors = sum(total_issues[k] for k in ['structure', 'json', 'yaml', 'broken_links'])
    total_warnings = total_issues['unused_images']

    if total_errors == 0 and total_warnings == 0:
        lines.append(format_success("All checks passed successfully! 🎉"))
    elif total_errors == 0:
        lines.append(format_warning("No errors found, but there are warnings to review."))
    else:
        lines.append(format_error(f"Found {total_errors} errors and {total_warnings} warnings."))

    return "\n".join(lines)
