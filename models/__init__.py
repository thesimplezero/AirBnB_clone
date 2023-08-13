#!/usr/bin/env python3
"""This module initializes the 'models' package."""
from file_storage import FileStorage
import os
import sys

# Get directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Append parent directory to sys.path
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

storage = FileStorage()
storage.reload()
