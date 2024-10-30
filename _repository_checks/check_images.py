"""
Validates image references in README files and checks for unused images.
"""
import os
import re
from common import setup_logging

def get_readme_images(readme_path):
    """
    Extract all image references from a README file
    
    Args:
        readme_path: Path to README.md file
    Returns:
        set: Set of image filenames referenced in README
    """
    if not os.path.exists(readme_path):
        return set()
        
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Find both Markdown and HTML image references
    md_images = re.findall(r'!\[.*?\]\((.*?)\)', content)
    html_images = re.findall(r'<img\s+[^>]*src="([^"]*)"', content)
    
    # Extract just the filenames from the paths
    images = set()
    for img in md_images + html_images:
        images.add(os.path.basename(img))
        
    return images

def check_images(component_path):
    """
    Check image references and files in a component
    
    Args:
        component_path: Path to component directory
    Returns:
        dict: Dictionary containing image-related issues
    """
    issues = {
        'missing_images': [],
        'unused_images': [],
        'broken_links': []
    }
    
    readme_path = os.path.join(component_path, 'README.md')
    images_dir = os.path.join(component_path, 'Images')
    
    # Get all images referenced in README
    referenced_images = get_readme_images(readme_path)
    
    # Get all actual image files
    existing_images = set()
    if os.path.exists(images_dir):
        for file in os.listdir(images_dir):
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg')):
                existing_images.add(file)
    
    # Check for missing and unused images
    for ref_img in referenced_images:
        if ref_img not in existing_images:
            issues['broken_links'].append(f"{readme_path} -> {ref_img}")
            
    for exist_img in existing_images:
        if exist_img not in referenced_images:
            issues['unused_images'].append(os.path.join('Images', exist_img))
            
    return issues

if __name__ == "__main__":
    logger = setup_logging()
    issues = check_images(".")
    if any(issues.values()):
        print("\nImage Issues Found:")
        if issues['broken_links']:
            print("\nBroken Links:")
            for link in issues['broken_links']:
                print(f"  - {link}")
        if issues['unused_images']:
            print("\nUnused Images:")
            for image in issues['unused_images']:
                print(f"  - {image}")
        exit(1)
    print("No image issues found.")
    exit(0)
