#!/usr/bin/env python3
"""
Configuration management script for Clive.

This script provides a command-line interface for managing the Clive configuration.
"""

import os
import sys

# Add the workspace directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.utils.cli import main

if __name__ == "__main__":
    main()
