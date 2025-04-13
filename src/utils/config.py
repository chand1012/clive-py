import json
from pathlib import Path
from typing import Optional

from pydantic import BaseModel, Field


class LLMConfig(BaseModel):
    """Configuration for an LLM model."""

    api_key: str = Field(description="The API key for the LLM")
    api_base: str = Field(description="The API base URL")
    model_id: str = Field(
        description="The ID for the model in LiteLLM format. provider/model-name"
    )


class EmbeddingConfig(BaseModel):
    """Configuration for an embedding model."""

    model_id: str = Field(
        description="The ID for the model in Ollama's format. model-name"
    )


class Settings(BaseModel):
    """Global settings for the application."""

    vision_llm: LLMConfig = Field(
        description="Vision LLM used for interpreting screenshots"
    )
    llm: LLMConfig = Field(description="LLM used for other tasks")
    embedding: EmbeddingConfig = Field(description="Embedding model configuration")


def get_config_dir() -> Path:
    """Get the configuration directory path."""
    config_dir = Path.home() / ".clive"
    config_dir.mkdir(exist_ok=True)
    return config_dir


def get_config_path() -> Path:
    """Get the configuration file path."""
    return get_config_dir() / "settings.json"


def load_settings() -> Settings:
    """Load settings from the configuration file."""
    config_path = get_config_path()

    # If the config file doesn't exist, create it with default settings
    if not config_path.exists():
        default_settings = Settings(
            vision_llm=LLMConfig(
                api_key="ollama",
                api_base="http://localhost:11434",
                model_id="ollama/gemma3:12b",
            ),
            llm=LLMConfig(
                api_key="ollama",
                api_base="http://localhost:11434",
                model_id="ollama/gemma3:12b",
            ),
            embedding=EmbeddingConfig(model_id="nomic-embed-text"),
        )
        save_settings(default_settings)
        return default_settings

    # Load settings from the config file
    with open(config_path, "r") as f:
        config_data = json.load(f)

    return Settings.model_validate(config_data)


def save_settings(settings: Settings) -> None:
    """Save settings to the configuration file."""
    config_path = get_config_path()

    with open(config_path, "w") as f:
        json.dump(settings.model_dump(), f, indent=2)


# Global settings instance
_settings: Optional[Settings] = None


def get_settings() -> Settings:
    """Get the global settings instance."""
    global _settings
    if _settings is None:
        _settings = load_settings()
    return _settings


def reload_settings() -> Settings:
    """Reload settings from the configuration file."""
    global _settings
    # Force a reload by calling load_settings directly
    _settings = None
    return get_settings()
