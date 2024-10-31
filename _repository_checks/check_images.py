"""
Validates image references in README files and checks for unused images.

This script performs two main checks:
1. Ensures all images referenced in README.md files actually exist
2. Identifies any images in the Images directory that aren't referenced in README.md

It handles both Markdown-style and HTML-style image references.
"""

# Standard library imports
import os  # File and directory operations
import re  # Regular expression support for parsing image references
from common import setup_logging  # Import shared logging configuration

def get_readme_images(readme_path):
    """
    Extract all image references from a README file.
    
    This function looks for two types of image references:
    1. Markdown format: ![alt text](image.png)
    2. HTML format: <img src="image.png" />
    
    Args:
        readme_path: Path to README.md file to check
        
    Returns:
        set: Set of unique image filenames referenced in README
             Note: Only the filename is returned, not the full path
    
    Example:
        For a README containing:
        ![Example](Images/example.png)
        <img src="Images/another.png" />
        
        Returns: {'example.png', 'another.png'}
    """
    # Return empty set if README doesn't exist
    if not os.path.exists(readme_path):
        return set()
    
    # Read the entire README file
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find image references using regex patterns
    # Markdown pattern: matches ![any text](filename)
    md_images = re.findall(r'!\[.*?\]\((.*?)\)', content)
    
    # HTML pattern: matches <img src="filename" ...>
    html_images = re.findall(r'<img\s+[^>]*src="([^"]*)"', content)
    
    # Combine all found images and extract just the filenames
    images = set()
    for img in md_images + html_images:
        # os.path.basename removes the path, leaving just the filename
        # e.g., 'Images/example.png' becomes 'example.png'
        images.add(os.path.basename(img))
    
    return images

def check_images(component_path):
    """
    Check image references and files in a component directory.
    
    This function performs two main checks:
    1. Verifies all referenced images exist
    2. Identifies any unused images
    
    Args:
        component_path: Path to the component directory to check
                       Expected structure:
                       component/
                       ├── README.md
                       └── Images/
                           ├── used.png
                           └── unused.png
    
    Returns:
        dict: Dictionary containing three types of issues:
              - missing_images: Images that should exist but don't
              - unused_images: Images that exist but aren't referenced
              - broken_links: Full details of broken image references
    
    Example return value:
        {
            'missing_images': ['missing.png'],
            'unused_images': ['Images/unused.png'],
            'broken_links': ['path/to/README.md -> missing.png']
        }
    """
    # Initialize dictionary to store all found issues
    issues = {
        'missing_images': [],  # Images referenced but not found
        'unused_images': [],   # Images found but not referenced
        'broken_links': []     # Full paths of broken references
    }
    
    # Construct paths to README and Images directory
    readme_path = os.path.join(component_path, 'README.md')
    images_dir = os.path.join(component_path, 'Images')
    
    # Get all images referenced in README
    referenced_images = get_readme_images(readme_path)
    
    # Get all actual image files from the Images directory
    existing_images = set()
    if os.path.exists(images_dir):
        for file in os.listdir(images_dir):
            # Check for common image file extensions
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg')):
                existing_images.add(file)
    
    # Find broken links (referenced but don't exist)
    for ref_img in referenced_images:
        if ref_img not in existing_images:
            issues['broken_links'].append(f"{readme_path} -> {ref_img}")
    
    # Find unused images (exist but not referenced)
    for exist_img in existing_images:
        if exist_img not in referenced_images:
            issues['unused_images'].append(os.path.join('Images', exist_img))
    
    return issues

# Script entry point - allows running this file directly for testing
if __name__ == "__main__":
    # Set up logging
    logger = setup_logging()
    
    # Check current directory
    issues = check_images(".")
    
    # Report any issues found
    if any(issues.values()):
        print("\nImage Issues Found:")
        
        # Report broken links (missing images)
        if issues['broken_links']:
            print("\nBroken Links:")
            for link in issues['broken_links']:
                print(f"  - {link}")
        
        # Report unused images
        if issues['unused_images']:
            print("\nUnused Images:")
            for image in issues['unused_images']:
                print(f"  - {image}")
        
        # Exit with error code if issues found
        exit(1)
    
    # No issues found
    print("No image issues found.")
    exit(0)