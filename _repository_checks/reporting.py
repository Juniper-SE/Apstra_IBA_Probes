"""
Enhanced reporting functionality with improved visual formatting.

This module handles all report generation and formatting for the validation tools.
It provides:
1. Color-coded output for different message types
2. Emoji indicators for status and categories
3. Consistent formatting for headers and sections
4. Structured reporting for different validation types
5. Summary statistics and final reports

The reporting is designed to be clear and visually appealing in terminal output,
using both colors and emoji to make different types of issues easily distinguishable.
"""

# Standard library imports
import os
from typing import Dict, List, Any  # Type hints for better code documentation
from datetime import datetime

# ANSI color codes for terminal output
class Colors:
    """
    ANSI escape codes for terminal color output.
    
    These codes will change the color of terminal text when printed:
    - Each code starts with \033[
    - The 'm' at the end indicates it's a color code
    - ENDC resets all formatting
    
    Note: These codes work in most modern terminals but may not work in all environments.
    """
    HEADER = '\033[95m'  # Pink - Used for main headers
    OKBLUE = '\033[94m'  # Blue - Used for information and subheaders
    OKGREEN = '\033[92m' # Green - Used for success messages
    WARNING = '\033[93m' # Yellow - Used for warnings
    FAIL = '\033[91m'    # Red - Used for errors
    ENDC = '\033[0m'     # Reset - Clears all formatting
    BOLD = '\033[1m'     # Bold - Used for emphasis

# Emoji indicators for different status types
EMOJI = {
    'success': '✅',  # Used for successful checks
    'error': '❌',    # Used for failed checks
    'warning': '⚠️',  # Used for warnings
    'info': 'ℹ️',     # Used for information
    'folder': '📁',   # Used for directory issues
    'file': '📄',     # Used for file issues
    'image': '🖼️',    # Used for image issues
    'json': '📊',     # Used for JSON file issues
    'yaml': '📝',     # Used for YAML file issues
    'check': '🔍'     # Used for validation indicators
}

def create_section_header(title: str) -> str:
    """
    Create a formatted section header with consistent styling.
    
    Creates a visually distinct header with:
    - Double line of equals signs above and below
    - Bold and colored text
    - Centered title
    
    Args:
        title (str): The title text for the header
        
    Returns:
        str: Formatted header string
        
    Example:
        ============================================================
        Title Here
        ============================================================
    """
    return f"\n{Colors.BOLD}{Colors.HEADER}{'='*60}{Colors.ENDC}\n{Colors.BOLD}{title}{Colors.ENDC}\n{Colors.BOLD}{Colors.HEADER}{'='*60}{Colors.ENDC}\n"

def create_subsection_header(title: str) -> str:
    """
    Create a formatted subsection header with different styling than main headers.
    
    Creates a visually distinct but subordinate header with:
    - Single line of dashes above and below
    - Blue coloring to distinguish from main headers
    
    Args:
        title (str): The title text for the subheader
        
    Returns:
        str: Formatted subheader string
        
    Example:
        ----------------------------------------
        Subsection Title Here
        ----------------------------------------
    """
    return f"\n{Colors.BOLD}{Colors.OKBLUE}{'-'*40}\n{title}\n{'-'*40}{Colors.ENDC}\n"

def format_error(message: str) -> str:
    """
    Format error messages in red with error emoji.
    
    Args:
        message (str): The error message to format
        
    Returns:
        str: Red-colored message prefixed with ❌
        
    Example:
        ❌ This is an error message
    """
    return f"{Colors.FAIL}{EMOJI['error']} {message}{Colors.ENDC}"

def format_warning(message: str) -> str:
    """
    Format warning messages in yellow with warning emoji.
    
    Args:
        message (str): The warning message to format
        
    Returns:
        str: Yellow-colored message prefixed with ⚠️
        
    Example:
        ⚠️ This is a warning message
    """
    return f"{Colors.WARNING}{EMOJI['warning']} {message}{Colors.ENDC}"

def format_success(message: str) -> str:
    """
    Format success messages in green with success emoji.
    
    Args:
        message (str): The success message to format
        
    Returns:
        str: Green-colored message prefixed with ✅
        
    Example:
        ✅ This is a success message
    """
    return f"{Colors.OKGREEN}{EMOJI['success']} {message}{Colors.ENDC}"

def format_info(message: str) -> str:
    """
    Format informational messages in blue with info emoji.
    
    Args:
        message (str): The informational message to format
        
    Returns:
        str: Blue-colored message prefixed with ℹ️
        
    Example:
        ℹ️ This is an informational message
    """
    return f"{Colors.OKBLUE}{EMOJI['info']} {message}{Colors.ENDC}"

def format_release_header(release: str) -> str:
    """
    Format a release section header with package emoji.
    
    Args:
        release (str): The release identifier (e.g., "release_4.2.1")
        
    Returns:
        str: Formatted header for release section
        
    Example:
        ============================================================
        📦 Checking Release: release_4.2.1
        ============================================================
    """
    return create_section_header(f"📦 Checking Release: {release}")

def format_component_header(component: str) -> str:
    """
    Format a component section header.
    
    Args:
        component (str): The component name
        
    Returns:
        str: Formatted header for component section
        
    Example:
        ----------------------------------------
        Checking Component: ComponentName
        ----------------------------------------
    """
    return create_subsection_header(f"Checking Component: {component}")

def format_structure_issues_content(issues: Dict[str, List[str]]) -> str:
    """
    Format directory structure issues content with proper indentation and icons.
    
    Formats each component's issues with:
    - Component name in bold
    - Folder emoji for component headers
    - Error emoji for each issue
    - Proper indentation for readability
    
    Args:
        issues (Dict[str, List[str]]): Dictionary mapping components to their issues
        
    Returns:
        str: Formatted structure issues content
        
    Example output:
        📁 ComponentName:
            ❌ Missing Content directory
            ❌ Missing Images directory
    """
    lines = []
    for component, component_issues in issues.items():
        lines.append(f"\n{EMOJI['folder']} {Colors.BOLD}{component}:{Colors.ENDC}")
        for issue in component_issues:
            lines.append(format_error(f"    {issue}"))
    return "\n".join(lines)

def format_json_yaml_issues_content(issues: Dict[str, List[str]]) -> str:
    """
    Format JSON and YAML validation issues with appropriate icons and grouping.
    
    Groups issues by file type (JSON/YAML) and formats each with:
    - Appropriate file type emoji
    - Error details with line numbers (if available)
    - Indented error messages for readability
    
    Args:
        issues (Dict[str, List[str]]): Dictionary containing 'invalid_json' and 'invalid_yaml' lists
        
    Returns:
        str: Formatted JSON/YAML issues content
        
    Example output:
        📊 Invalid JSON files:
            ❌ config.json at line 15: Missing comma
        
        📝 Invalid YAML files:
            ❌ settings.yaml: Invalid indentation
    """
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
    """
    Format image reference issues with categorization and proper spacing.
    
    Separates and formats two types of image issues:
    1. Broken links (errors) - Images referenced but not found
    2. Unused images (warnings) - Images present but not referenced
    
    Args:
        issues (Dict[str, List[str]]): Dictionary containing 'broken_links' and 'unused_images' lists
        
    Returns:
        str: Formatted image issues content
        
    Example output:
        🖼️ Broken Links:
            ❌ README.md -> missing_image.png
        
        🖼️ Unused Images:
            ⚠️ Images/unused_image.png
    """
    lines = []
    if issues['broken_links']:
        lines.append(f"{EMOJI['image']} {Colors.BOLD}Broken Links:{Colors.ENDC}")
        for link in issues['broken_links']:
            lines.append(format_error(f"    {link}"))
            
    if issues['unused_images']:
        if issues['broken_links']:
            lines.append("")  # Add spacing between sections
        lines.append(f"{EMOJI['image']} {Colors.BOLD}Unused Images:{Colors.ENDC}")
        for image in issues['unused_images']:
            lines.append(format_warning(f"    {image}"))
    return "\n".join(lines)

def format_full_report(release: str, results: Dict[str, Any]) -> str:
    """
    Generate a comprehensive report for a single release with all validation results.
    
    Creates a structured report with sections for:
    1. Release header
    2. Structure validation results
    3. JSON/YAML validation results
    4. Image validation results per component
    
    Each section is visually separated and contains either issues found or success messages.
    
    Args:
        release (str): Release identifier (e.g., "release_4.2.1")
        results (Dict[str, Any]): Dictionary containing all validation results:
            - structure_issues: Directory structure validation results
            - json_yaml_issues: File format validation results
            - image_issues: Image reference validation results by component
            
    Returns:
        str: Complete formatted report for the release
        
    Example structure:
        ============================================================
        📦 Checking Release: release_4.2.1
        ============================================================
        
        ============================================================
        Structure Validation
        ============================================================
        [Structure issues or success message]
        
        ============================================================
        JSON/YAML Validation
        ============================================================
        [JSON/YAML issues or success message]
        
        ============================================================
        Image Validation
        ============================================================
        [Component-wise image validation results]
    """
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
    """
    Generate a final summary of all validation results across all releases.
    
    Calculates and formats:
    1. Scope of validation (releases and components checked)
    2. Total count of each type of error
    3. Total count of warnings
    4. Final status message based on error/warning counts
    
    Args:
        all_results (Dict[str, Dict[str, Any]]): Results from all releases
            Key: Release identifier
            Value: Dictionary containing that release's validation results
            
    Returns:
        str: Formatted summary report
        
    Example output:
        ============================================================
        Final Summary
        ============================================================
        ℹ️ Scope:
            Releases checked: 2
            Components checked: 8
        
        ❌ Errors Found:
            Structure issues: 3
            Invalid JSON files: 1
            Invalid YAML files: 0
            Broken image links: 2
        
        ⚠️ Warnings Found:
            Unused images: 4
        
        ❌ Found 6 errors and 4 warnings.
    """
    # Initialize counters for all issue types
    total_issues = {
        'structure': 0,
        'json': 0,
        'yaml': 0,
        'broken_links': 0,
        'unused_images': 0,
        'components_checked': 0,
        'releases_checked': len(all_results)
    }
    
    # Collect counts from all releases
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

    # Format the summary report
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

    # Calculate totals and add final status message
    total_errors = sum(total_issues[k] for k in ['structure', 'json', 'yaml', 'broken_links'])
    total_warnings = total_issues['unused_images']

    if total_errors == 0 and total_warnings == 0:
        lines.append(format_success("All checks passed successfully! 🎉"))
    elif total_errors == 0:
        lines.append(format_warning("No errors found, but there are warnings to review."))
    else:
        lines.append(format_error(f"Found {total_errors} errors and {total_warnings} warnings."))

    return "\n".join(lines)