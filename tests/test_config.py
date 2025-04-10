import json
import os
import tempfile
from pathlib import Path
from unittest import mock

import pytest

from src.utils.config import (
    EmbeddingConfig,
    LLMConfig,
    Settings,
    get_config_dir,
    get_config_path,
    get_settings,
    load_settings,
    reload_settings,
    save_settings,
)


def test_config_models():
    """Test that the configuration models work correctly."""
    # Test LLMConfig
    llm_config = LLMConfig(
        api_key="test_key",
        api_base="http://test.com",
        model_id="test/model"
    )
    assert llm_config.api_key == "test_key"
    assert llm_config.api_base == "http://test.com"
    assert llm_config.model_id == "test/model"

    # Test EmbeddingConfig
    embedding_config = EmbeddingConfig(
        model_id="test-model"
    )
    assert embedding_config.model_id == "test-model"

    # Test Settings
    settings = Settings(
        vision_llm=llm_config,
        llm=llm_config,
        embedding=embedding_config
    )
    assert settings.vision_llm == llm_config
    assert settings.llm == llm_config
    assert settings.embedding == embedding_config


@mock.patch("src.utils.config.get_config_path")
def test_load_and_save_settings(mock_get_config_path):
    """Test loading and saving settings."""
    # Create a temporary file for testing
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_path = Path(temp_file.name)

    try:
        # Mock the config path to use our temporary file
        mock_get_config_path.return_value = temp_path

        # Test saving settings
        settings = Settings(
            vision_llm=LLMConfig(
                api_key="test_key",
                api_base="http://test.com",
                model_id="test/model"
            ),
            llm=LLMConfig(
                api_key="test_key2",
                api_base="http://test2.com",
                model_id="test/model2"
            ),
            embedding=EmbeddingConfig(
                model_id="test-model"
            )
        )
        save_settings(settings)

        # Verify the file was created with the correct content
        assert temp_path.exists()
        with open(temp_path, "r") as f:
            saved_data = json.load(f)

        assert saved_data["vision_llm"]["api_key"] == "test_key"
        assert saved_data["llm"]["api_base"] == "http://test2.com"
        assert saved_data["embedding"]["model_id"] == "test-model"

        # Test loading settings
        loaded_settings = load_settings()
        assert loaded_settings.vision_llm.api_key == "test_key"
        assert loaded_settings.llm.api_base == "http://test2.com"
        assert loaded_settings.embedding.model_id == "test-model"

    finally:
        # Clean up the temporary file
        if temp_path.exists():
            os.unlink(temp_path)


@mock.patch("src.utils.config.get_config_path")
def test_default_settings_creation(mock_get_config_path):
    """Test that default settings are created if the config file doesn't exist."""
    # Create a temporary path that doesn't exist
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir) / "settings.json"

        # Mock the config path to use our temporary file
        mock_get_config_path.return_value = temp_path

        # Load settings (should create default settings)
        settings = load_settings()

        # Verify default values
        assert settings.vision_llm.api_key == "ollama"
        assert settings.vision_llm.api_base == "http://localhost:11434"
        assert settings.vision_llm.model_id == "ollama/gemma3:12b"
        assert settings.llm.api_key == "ollama"
        assert settings.llm.api_base == "http://localhost:11434"
        assert settings.llm.model_id == "ollama/gemma3:12b"
        assert settings.embedding.model_id == "nomic-embed-text"

        # Verify the file was created
        assert temp_path.exists()


@mock.patch("src.utils.config.load_settings")
def test_get_settings_caching(mock_load_settings):
    """Test that get_settings caches the settings."""
    # Create mock settings
    mock_settings = Settings(
        vision_llm=LLMConfig(
            api_key="test_key",
            api_base="http://test.com",
            model_id="test/model"
        ),
        llm=LLMConfig(
            api_key="test_key2",
            api_base="http://test2.com",
            model_id="test/model2"
        ),
        embedding=EmbeddingConfig(
            model_id="test-model"
        )
    )
    mock_load_settings.return_value = mock_settings

    # Call get_settings twice
    settings1 = get_settings()
    settings2 = get_settings()

    # Verify that load_settings was only called once
    mock_load_settings.assert_called_once()

    # Verify that the same settings object is returned
    assert settings1 is settings2


@mock.patch("src.utils.config.load_settings")
def test_reload_settings(mock_load_settings):
    """Test that reload_settings reloads the settings."""
    # Create mock settings
    mock_settings1 = Settings(
        vision_llm=LLMConfig(
            api_key="test_key",
            api_base="http://test.com",
            model_id="test/model"
        ),
        llm=LLMConfig(
            api_key="test_key2",
            api_base="http://test2.com",
            model_id="test/model2"
        ),
        embedding=EmbeddingConfig(
            model_id="test-model"
        )
    )
    mock_settings2 = Settings(
        vision_llm=LLMConfig(
            api_key="test_key3",
            api_base="http://test3.com",
            model_id="test/model3"
        ),
        llm=LLMConfig(
            api_key="test_key4",
            api_base="http://test4.com",
            model_id="test/model4"
        ),
        embedding=EmbeddingConfig(
            model_id="test-model2"
        )
    )

    # First call to load_settings returns mock_settings1
    # Second call returns mock_settings2
    mock_load_settings.side_effect = [mock_settings1, mock_settings2]

    # Reset the global settings variable
    import src.utils.config
    src.utils.config._settings = None

    # Call get_settings to initialize the cache
    settings1 = get_settings()
    assert settings1 == mock_settings1

    # Call reload_settings to reload the settings
    # This should set _settings to None and then call get_settings again
    settings2 = reload_settings()
    assert settings2 == mock_settings2

    # Verify that load_settings was called twice
    assert mock_load_settings.call_count == 2

    # Verify that different settings objects are returned
    assert settings1 is not settings2
    assert settings1.vision_llm.api_key == "test_key"
    assert settings2.vision_llm.api_key == "test_key3"
