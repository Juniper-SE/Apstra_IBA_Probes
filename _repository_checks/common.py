"""
Common utilities shared across all repository checking scripts.
Provides logging setup and basic repository information functions.
"""
import os
import logging
from pathlib import Path

def setup_logging():
    """
    Configure and setup logging with a standard format.
    Returns:
        logger: Configured logging object with standard formatting
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger('repo-check')

def get_release_type(release_dir):
    """
    Determine the type of release based on directory name.
    We have two types: legacy (4.2.1) and modern (5.0.0+)
    
    Args:
        release_dir: Name of the release directory
    Returns:
        str: 'legacy' for 4.2.1, 'modern' for 5.0.0 and newer
    """
    if "4.2.1" in release_dir:
        return "legacy"
    return "modern"

def get_all_releases(repo_path):
    """
    Find all release directories in the repository.
    Looks for directories starting with 'release_'
    
    Args:
        repo_path: Path to the repository root
    Returns:
        list: List of release directory names, sorted
    """
    releases = []
    for item in os.listdir(repo_path):
        if item.startswith('release_') and os.path.isdir(os.path.join(repo_path, item)):
            releases.append(item)
    return sorted(releases)
