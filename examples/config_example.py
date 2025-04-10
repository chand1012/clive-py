#!/usr/bin/env python3
"""
Example script demonstrating how to use the configuration system.
"""

import json
import os
import sys
from pathlib import Path

# Add the workspace directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.utils.config import (
    EmbeddingConfig,
    LLMConfig,
    Settings,
    get_settings,
    save_settings,
)


def main():
    """Run the example."""
    # Get the current settings
    settings = get_settings()
    print("Current settings:")
    print(json.dumps(settings.model_dump(), indent=2))

    # Update the settings
    settings.llm.model_id = "ollama/llama3:8b"
    settings.vision_llm.model_id = "ollama/llama3:8b"
    settings.embedding.model_id = "nomic-embed-text:latest"

    # Save the settings
    save_settings(settings)
    print("\nSettings updated.")

    # Reload the settings
    settings = get_settings()
    print("\nUpdated settings:")
    print(json.dumps(settings.model_dump(), indent=2))

    # Reset to default settings
    default_settings = Settings(
        vision_llm=LLMConfig(
            api_key="ollama",
            api_base="http://localhost:11434",
            model_id="ollama/gemma3:12b"
        ),
        llm=LLMConfig(
            api_key="ollama",
            api_base="http://localhost:11434",
            model_id="ollama/gemma3:12b"
        ),
        embedding=EmbeddingConfig(
            model_id="nomic-embed-text"
        )
    )
    save_settings(default_settings)
    print("\nSettings reset to default values.")


if __name__ == "__main__":
    main()
