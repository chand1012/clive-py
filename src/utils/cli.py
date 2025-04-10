import json
from typing import Optional

import fire

from src.utils.config import (
    EmbeddingConfig,
    LLMConfig,
    Settings,
    get_settings,
    save_settings,
)


class ConfigCLI:
    """Command-line interface for managing configuration."""

    def show(self) -> None:
        """Show the current configuration."""
        settings = get_settings()
        print(json.dumps(settings.model_dump(), indent=2))

    def set_vision_llm(
        self,
        api_key: Optional[str] = None,
        api_base: Optional[str] = None,
        model_id: Optional[str] = None,
    ) -> None:
        """Set the vision LLM configuration.

        Args:
            api_key: The API key for the LLM
            api_base: The API base URL
            model_id: The ID for the model in LiteLLM format. provider/model-name
        """
        settings = get_settings()

        if api_key is not None:
            settings.vision_llm.api_key = api_key

        if api_base is not None:
            settings.vision_llm.api_base = api_base

        if model_id is not None:
            settings.vision_llm.model_id = model_id

        save_settings(settings)
        print("Vision LLM configuration updated.")

    def set_llm(
        self,
        api_key: Optional[str] = None,
        api_base: Optional[str] = None,
        model_id: Optional[str] = None,
    ) -> None:
        """Set the LLM configuration.

        Args:
            api_key: The API key for the LLM
            api_base: The API base URL
            model_id: The ID for the model in LiteLLM format. provider/model-name
        """
        settings = get_settings()

        if api_key is not None:
            settings.llm.api_key = api_key

        if api_base is not None:
            settings.llm.api_base = api_base

        if model_id is not None:
            settings.llm.model_id = model_id

        save_settings(settings)
        print("LLM configuration updated.")

    def set_embedding(
        self,
        model_id: Optional[str] = None,
    ) -> None:
        """Set the embedding model configuration.

        Args:
            model_id: The ID for the model in Ollama's format. model-name
        """
        settings = get_settings()

        if model_id is not None:
            settings.embedding.model_id = model_id

        save_settings(settings)
        print("Embedding model configuration updated.")

    def reset(self) -> None:
        """Reset the configuration to default values."""
        settings = Settings(
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
        save_settings(settings)
        print("Configuration reset to default values.")


def main() -> None:
    """Run the configuration CLI."""
    fire.Fire(ConfigCLI)
