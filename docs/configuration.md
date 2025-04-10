# Configuration System

Clive uses a configuration system to store and manage settings. The configuration is stored in a JSON file at `~/.clive/settings.json`.

## Configuration Structure

The configuration file has the following structure:

```json
{
  "vision_llm": {
    "api_key": "your_api_key",
    "api_base": "https://api.example.com",
    "model_id": "provider/model-name"
  },
  "llm": {
    "api_key": "your_api_key",
    "api_base": "https://api.example.com",
    "model_id": "provider/model-name"
  },
  "embedding": {
    "model_id": "model-name"
  }
}
```

### Vision LLM

The Vision LLM is used for interpreting screenshots and other visual content.

- `api_key`: The API key for the LLM
- `api_base`: The API base URL
- `model_id`: The ID for the model in [LiteLLM format](https://docs.litellm.ai/docs/#basic-usage). `provider/model-name`

### LLM

The LLM is used for other tasks such as text processing and generation.

- `api_key`: The API key for the LLM
- `api_base`: The API base URL
- `model_id`: The ID for the model in [LiteLLM format](https://docs.litellm.ai/docs/#basic-usage). `provider/model-name`

### Embedding Model

The embedding model is used for generating vector embeddings of text.

- `model_id`: The ID for the model in Ollama's format. `model-name`

## Managing Configuration

### Command Line Interface

You can manage the configuration using the `config.py` script in the `scripts` directory:

```bash
# Show the current configuration
python scripts/config.py show

# Set the vision LLM configuration
python scripts/config.py set_vision_llm --api_key=your_api_key --api_base=https://api.example.com --model_id=provider/model-name

# Set the LLM configuration
python scripts/config.py set_llm --api_key=your_api_key --api_base=https://api.example.com --model_id=provider/model-name

# Set the embedding model configuration
python scripts/config.py set_embedding --model_id=model-name

# Reset the configuration to default values
python scripts/config.py reset
```

### Programmatic Access

You can also manage the configuration programmatically:

```python
from src.utils.config import get_settings, save_settings

# Get the current settings
settings = get_settings()

# Update the settings
settings.llm.model_id = "ollama/llama3:8b"
settings.vision_llm.model_id = "ollama/llama3:8b"
settings.embedding.model_id = "nomic-embed-text:latest"

# Save the settings
save_settings(settings)
```

## Environment Variables

The configuration system also respects environment variables. If an environment variable is set, it takes precedence over the value in the configuration file.

The following environment variables are supported:

- `LLM_API_KEY`: The API key for the LLM
- `LLM_BASE_URL`: The API base URL for the LLM
- `LLM_MODEL`: The model ID for the LLM
- `VISION_LLM_API_KEY`: The API key for the Vision LLM
- `VISION_LLM_BASE_URL`: The API base URL for the Vision LLM
- `VISION_LLM_MODEL`: The model ID for the Vision LLM
- `EMBEDDING_MODEL`: The model ID for the embedding model

## Default Values

If the configuration file doesn't exist, the following default values are used:

- Vision LLM:
  - `api_key`: "ollama"
  - `api_base`: "http://localhost:11434"
  - `model_id`: "ollama/gemma3:12b"
- LLM:
  - `api_key`: "ollama"
  - `api_base`: "http://localhost:11434"
  - `model_id`: "ollama/gemma3:12b"
- Embedding:
  - `model_id`: "nomic-embed-text"
