"""
Main script that runs all repository checks and generates a comprehensive report.
"""
import os
from common import setup_logging, get_all_releases
from check_structure import check_release_structure
from check_json_yaml import validate_json_yaml_files
from check_images import check_images
from reporting import (
    format_full_report, 
    generate_summary_tally,
    format_error,
    create_section_header
)

def main():
    """
    Main function to run all checks on the repository
    Returns:
        int: 0 if all checks pass, 1 if any issues found
    """
    logger = setup_logging()
    repo_path = "."  # Current directory, modify as needed
    
    print(create_section_header("Repository Validation"))
    
    # Get all releases
    releases = get_all_releases(repo_path)
    if not releases:
        print(format_error("No release directories found!"))
        return 1
        
    all_results = {}
    
    # Check each release
    for release in releases:
        release_path = os.path.join(repo_path, release)
        results = {
            'structure_issues': check_release_structure(release_path),
            'json_yaml_issues': validate_json_yaml_files(release_path),
            'image_issues': {}
        }
        
        # Check images for each component
        for component in os.listdir(release_path):
            component_path = os.path.join(release_path, component)
            if os.path.isdir(component_path):
                results['image_issues'][component] = check_images(component_path)
        
        # Store results for summary
        all_results[release] = results
        
        # Print individual release report
        print(format_full_report(release, results))
    
    # Print summary tally
    print(generate_summary_tally(all_results))
    
    # Determine if there were any errors
    has_errors = any(
        bool(results['structure_issues']) or
        any(results['json_yaml_issues'].values()) or
        any(any(issues.values()) for issues in results['image_issues'].values())
        for results in all_results.values()
    )
    
    return 1 if has_errors else 0

if __name__ == "__main__":
    exit(main())
