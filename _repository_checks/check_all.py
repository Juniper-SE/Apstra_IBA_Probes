"""
Main script that runs all repository checks and generates a comprehensive report.

This script is the primary entry point for the repository validation tool.
It orchestrates all checks including:
- Directory structure validation
- JSON/YAML file validation
- Image reference validation

The script processes each release directory and generates both individual reports
and a final summary of all issues found.
"""

# Standard library imports
import os

# Local imports for different validation components
from common import setup_logging, get_all_releases  # Basic utilities
from check_structure import check_release_structure  # Directory structure validation
from check_json_yaml import validate_json_yaml_files  # File format validation
from check_images import check_images  # Image reference validation
from reporting import (  # Report generation utilities
    format_full_report, 
    generate_summary_tally,
    format_error,
    create_section_header
)

def main():
    """
    Main function to run all repository validation checks.
    
    This function:
    1. Sets up logging
    2. Finds all release directories
    3. For each release:
        - Validates directory structure
        - Checks JSON/YAML file syntax
        - Validates image references
    4. Generates both individual and summary reports
    
    Returns:
        int: Exit code
            0: All checks passed successfully
            1: Issues found or errors occurred
    """
    # Initialize logging for the validation process
    logger = setup_logging()
    
    # Set root path for repository (current directory by default)
    repo_path = "."  # Can be modified if needed for different directory
    
    # Create and display the main header for the validation report
    print(create_section_header("Repository Validation"))
    
    # Find all release directories in the repository
    releases = get_all_releases(repo_path)
    if not releases:
        # Exit if no release directories are found
        print(format_error("No release directories found!"))
        return 1
        
    # Dictionary to store results for all releases
    all_results = {}
    
    # Process each release directory
    for release in releases:
        # Construct full path to the release directory
        release_path = os.path.join(repo_path, release)
        
        # Run all validation checks for this release
        results = {
            # Check directory structure (Content, Images, etc.)
            'structure_issues': check_release_structure(release_path),
            
            # Validate all JSON and YAML files in the release
            'json_yaml_issues': validate_json_yaml_files(release_path),
            
            # Prepare dictionary for image validation results
            'image_issues': {}
        }
        
        # Check images for each component within the release
        for component in os.listdir(release_path):
            component_path = os.path.join(release_path, component)
            if os.path.isdir(component_path):
                # Validate image references and find unused images
                results['image_issues'][component] = check_images(component_path)
        
        # Store results for this release for later summary
        all_results[release] = results
        
        # Generate and display the report for this release
        print(format_full_report(release, results))
    
    # After all releases are checked, display the summary
    print(generate_summary_tally(all_results))
    
    # Determine if any errors were found across all checks
    has_errors = any(
        bool(results['structure_issues']) or  # Any structure issues
        any(results['json_yaml_issues'].values()) or  # Any JSON/YAML issues
        any(any(issues.values()) for issues in results['image_issues'].values())  # Any image issues
        for results in all_results.values()
    )
    
    # Return appropriate exit code based on validation results
    return 1 if has_errors else 0

# Script entry point
if __name__ == "__main__":
    # Run main function and use its return value as exit code
    exit(main())