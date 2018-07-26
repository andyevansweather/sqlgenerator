"""Validates if the SQL directory exists,
 but if it doesn't, go and create it"""

import os


def validate_directory_exists():
    """
    Checks if download directory is there and if not makes one
    :return:
    """
    downloads_dir = 'static/downloads'
    if not os.path.exists(downloads_dir):
        os.makedirs(downloads_dir)
