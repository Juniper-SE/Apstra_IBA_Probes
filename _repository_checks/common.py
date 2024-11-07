"""
Common utilities shared across all repository checking scripts.
Provides logging setup and basic repository information functions.

This module serves as the foundation for the repository checking system, providing:
1. Standardized logging configuration
2. Release type determination (legacy vs modern)
3. Release directory discovery

These utilities are used by all other validation scripts to ensure consistent
behavior and reduce code duplication.
"""

# Standard library imports
import os       # File and directory operations
import logging  # Logging functionality
from pathlib import Path  # Modern path manipulation

def setup_logging():
    """
    Configure and setup logging with a standard format.
    
    This function sets up a consistent logging configuration used across
    all validation scripts. It ensures that log messages are formatted
    uniformly and contain necessary information for debugging.
    
    Configuration:
        - Level: INFO (shows general operation information)
        - Format: timestamp - level - message
        - Logger name: 'repo-check' (identifies our application)
    
    Returns:
        logger: Configured logging object with standard formatting
    
    Example usage:
        >>> logger = setup_logging()
        >>> logger.info("Starting validation")
        2024-10-31 10:00:00,000 - INFO - Starting validation
    """
    logging.basicConfig(
        level=logging.INFO,  # Show all info-level and above messages
        format='%(asctime)s - %(levelname)s - %(message)s'  # Standard format with timestamp
    )
    return logging.getLogger('repo-check')

def get_release_type(release_dir):
    """
    Determine the type of release based on directory name.
    
    The repository contains two types of releases with different structures:
    1. Legacy (4.2.1): More complex structure with specific subdirectories
    2. Modern (5.0.0+): Simplified structure with fewer requirements
    
    Args:
        release_dir (str): Name of the release directory
                          Expected format: "release_X.Y.Z"
                          Example: "release_4.2.1" or "release_5.0.0"
    
    Returns:
        str: Release type identifier
            "legacy" - for release 4.2.1
            "modern" - for release 5.0.0 and newer
    
    Example usage:
        >>> get_release_type("release_4.2.1")
        'legacy'
        >>> get_release_type("release_5.0.0")
        'modern'
        >>> get_release_type("release_5.1.0")
        'modern'
    """
    if "4.2.1" in release_dir:
        return "legacy"
    return "modern"

def get_all_releases(repo_path):
    """
    Find all release directories in the repository.
    
    Scans the repository root directory for release directories that follow
    the naming convention "release_X.Y.Z" (e.g., release_4.2.1).
    
    Args:
        repo_path (str): Path to the repository root directory
                        Can be relative or absolute path
    
    Returns:
        list: Sorted list of release directory names
              Example: ["release_4.2.1", "release_5.0.0"]
              Empty list if no release directories found
    
    Note:
        - Only includes directories (not files)
        - Must start with "release_"
        - Returns sorted list for consistent processing order
    
    Example usage:
        >>> get_all_releases("/path/to/repo")
        ['release_4.2.1', 'release_5.0.0', 'release_5.1.0']
        
        >>> get_all_releases("/empty/repo")
        []
    
    Directory structure example:
        repo/
        ├── release_4.2.1/        # ✓ Included
        ├── release_5.0.0/        # ✓ Included
        ├── old_release_3.0.0/    # ✗ Not included (wrong prefix)
        └── release_note.txt      # ✗ Not included (not a directory)
    """
    releases = []
    
    # Scan directory for release folders
    for item in os.listdir(repo_path):
        # Check if item is a directory and starts with "release_"
        if item.startswith('release_') and os.path.isdir(os.path.join(repo_path, item)):
            releases.append(item)
    
    # Return sorted list for consistent ordering
    return sorted(releases)