"""
Validates the directory structure of repository components.
Handles both 4.2.1 and 5.0.0+ structures correctly.
"""
import os
from common import setup_logging, get_release_type

def check_legacy_structure(component_path):
    """
    Check directory structure for 4.2.1 release format
    
    Expected structure:
    component/
    ├── Content/
    │   ├── configlets/
    │   ├── dashboards/
    │   ├── probes/
    │   ├── property-sets/
    │   ├── telemetry-collectors/
    │   ├── telemetry-service-definitions/
    │   └── widgets/
    ├── Images/
    └── README.md
    
    Args:
        component_path: Path to component directory
    Returns:
        list: List of issues found
    """
    issues = []
    
    # Check for required top-level directories
    required_dirs = ['Content', 'Images']
    for required_dir in required_dirs:
        if not os.path.isdir(os.path.join(component_path, required_dir)):
            issues.append(f"Missing {required_dir} directory")
    
    # Check Content subdirectories if Content exists
    content_path = os.path.join(component_path, 'Content')
    if os.path.isdir(content_path):
        required_content_dirs = [
            'configlets',
            'dashboards',
            'probes',
            'property-sets',
            'telemetry-collectors',
            'telemetry-service-definitions',
            'widgets'
        ]
        for required_dir in required_content_dirs:
            if not os.path.isdir(os.path.join(content_path, required_dir)):
                issues.append(f"Missing Content/{required_dir} directory")
    
    return issues

def check_modern_structure(component_path):
    """
    Check directory structure for 5.0.0+ release format
    
    Expected structure:
    component/
    ├── Content/
    ├── Images/
    └── README.md
    
    Args:
        component_path: Path to component directory
    Returns:
        list: List of issues found
    """
    issues = []
    
    # Check for required directories
    required_dirs = ['Content', 'Images']
    for required_dir in required_dirs:
        if not os.path.isdir(os.path.join(component_path, required_dir)):
            issues.append(f"Missing {required_dir} directory")
    
    return issues

def check_release_structure(release_path):
    """
    Main function to check release structure
    
    Args:
        release_path: Path to release directory
    Returns:
        dict: Dictionary of issues found per component
    """
    logger = setup_logging()
    issues = {}
    
    release_type = get_release_type(release_path)
    
    for component in os.listdir(release_path):
        component_path = os.path.join(release_path, component)
        if not os.path.isdir(component_path):
            continue
            
        component_issues = []
        
        # Check README
        if not os.path.exists(os.path.join(component_path, 'README.md')):
            component_issues.append("Missing README.md")
        
        # Check structure based on release type
        if release_type == "legacy":
            component_issues.extend(check_legacy_structure(component_path))
        else:
            component_issues.extend(check_modern_structure(component_path))
            
        if component_issues:
            issues[component] = component_issues
    
    return issues

if __name__ == "__main__":
    logger = setup_logging()
    issues = check_release_structure(".")
    if issues:
        print("\nStructure Issues Found:")
        for component, component_issues in issues.items():
            print(f"\n{component}:")
            for issue in component_issues:
                print(f"  - {issue}")
        exit(1)
    print("No structure issues found.")
    exit(0)
