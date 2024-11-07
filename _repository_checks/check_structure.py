"""
Validates the directory structure of repository components.
Handles both 4.2.1 and 5.0.0+ structures correctly.

This script validates two different directory structures:
1. Legacy (4.2.1): Complex structure with specific Content subdirectories
2. Modern (5.0.0+): Simplified structure with just Content and Images

Each component in a release must follow its respective structure based on the release version.
"""

# Standard library imports
import os  # File and directory operations
from common import setup_logging, get_release_type  # Import shared utilities

def check_legacy_structure(component_path):
    """
    Check directory structure for 4.2.1 release format (Legacy).
    
    Expected structure:
    component/
    ├── Content/              # Required: Contains all configuration files
    │   ├── configlets/       # Required: Network device configurations
    │   ├── dashboards/       # Required: Dashboard definitions
    │   ├── probes/          # Required: Data collection probes
    │   ├── property-sets/    # Required: Property configurations
    │   ├── telemetry-collectors/        # Required: Data collectors
    │   ├── telemetry-service-definitions/# Required: Service definitions
    │   └── widgets/         # Required: Dashboard widgets
    ├── Images/              # Required: Documentation images
    └── README.md           # Required: Component documentation
    
    Args:
        component_path (str): Full path to the component directory being checked
        
    Returns:
        list: List of strings describing any missing or invalid directories
              Empty list if structure is valid
    
    Example:
        >>> check_legacy_structure("/path/to/component")
        ["Missing Content/widgets directory", "Missing Images directory"]
    """
    issues = []
    
    # First check top-level required directories
    required_dirs = ['Content', 'Images']
    for required_dir in required_dirs:
        dir_path = os.path.join(component_path, required_dir)
        if not os.path.isdir(dir_path):
            issues.append(f"Missing {required_dir} directory")
    
    # If Content exists, check its required subdirectories
    content_path = os.path.join(component_path, 'Content')
    if os.path.isdir(content_path):
        # List of all required subdirectories within Content
        required_content_dirs = [
            'configlets',            # Network device configurations
            'dashboards',            # Dashboard definitions
            'probes',                # Data collection probes
            'property-sets',         # Property configurations
            'telemetry-collectors',  # Data collectors
            'telemetry-service-definitions',  # Service definitions
            'widgets'                # Dashboard widgets
        ]
        # Check each required subdirectory
        for required_dir in required_content_dirs:
            dir_path = os.path.join(content_path, required_dir)
            if not os.path.isdir(dir_path):
                issues.append(f"Missing Content/{required_dir} directory")
    
    return issues

def check_modern_structure(component_path):
    """
    Check directory structure for 5.0.0+ release format (Modern).
    
    Expected structure:
    component/
    ├── Content/     # Required: Contains configuration files
    ├── Images/      # Required: Documentation images
    └── README.md    # Required: Component documentation
    
    The modern structure is simplified compared to legacy,
    requiring only the main Content and Images directories.
    
    Args:
        component_path (str): Full path to the component directory being checked
        
    Returns:
        list: List of strings describing any missing or invalid directories
              Empty list if structure is valid
    
    Example:
        >>> check_modern_structure("/path/to/component")
        ["Missing Content directory"]
    """
    issues = []
    
    # Check for required directories (simpler structure than legacy)
    required_dirs = ['Content', 'Images']
    for required_dir in required_dirs:
        dir_path = os.path.join(component_path, required_dir)
        if not os.path.isdir(dir_path):
            issues.append(f"Missing {required_dir} directory")
    
    return issues

def check_release_structure(release_path):
    """
    Main function to check release structure for all components.
    
    This function:
    1. Determines the release type (legacy or modern)
    2. Checks each component's structure accordingly
    3. Verifies README.md existence
    4. Collects all issues found
    
    Args:
        release_path (str): Path to the release directory to check
                           (e.g., "/path/to/release_4.2.1")
    
    Returns:
        dict: Dictionary mapping component names to their issues
              Only components with issues are included
    
    Example:
        {
            'Component1': ['Missing README.md', 'Missing Content/widgets directory'],
            'Component2': ['Missing Images directory']
        }
    """
    logger = setup_logging()
    issues = {}
    
    # Determine release type to know which structure to check against
    release_type = get_release_type(release_path)
    
    # Check each component in the release
    for component in os.listdir(release_path):
        component_path = os.path.join(release_path, component)
        
        # Skip if not a directory (only checking components)
        if not os.path.isdir(component_path):
            continue
            
        component_issues = []
        
        # Check README.md existence (required for all components)
        readme_path = os.path.join(component_path, 'README.md')
        if not os.path.exists(readme_path):
            component_issues.append("Missing README.md")
        
        # Apply appropriate structure check based on release type
        if release_type == "legacy":
            component_issues.extend(check_legacy_structure(component_path))
        else:
            component_issues.extend(check_modern_structure(component_path))
            
        # Only store components that have issues
        if component_issues:
            issues[component] = component_issues
    
    return issues

# Script entry point - allows running this file directly for testing
if __name__ == "__main__":
    logger = setup_logging()
    issues = check_release_structure(".")
    
    if issues:
        print("\nStructure Issues Found:")
        # Print issues grouped by component
        for component, component_issues in issues.items():
            print(f"\n{component}:")
            for issue in component_issues:
                print(f"  - {issue}")
        exit(1)
    
    print("No structure issues found.")
    exit(0)