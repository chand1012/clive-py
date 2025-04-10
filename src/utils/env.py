import os

from dotenv import load_dotenv

from src.utils.config import get_settings

load_dotenv()

# Load settings from config file
settings = get_settings()

# LLM_BASE_URL is the base URL for the LLM
# Environment variables take precedence over config file
LLM_BASE_URL = os.getenv("LLM_BASE_URL", settings.llm.api_base)

# LLM_API_KEY is the API key for the LLM
LLM_API_KEY = os.getenv("LLM_API_KEY", settings.llm.api_key)

# LLM_MODEL is the model to use for the LLM
LLM_MODEL = os.getenv("LLM_MODEL", settings.llm.model_id)

# VISION_LLM_BASE_URL is the base URL for the Vision LLM
VISION_LLM_BASE_URL = os.getenv("VISION_LLM_BASE_URL", settings.vision_llm.api_base)

# VISION_LLM_API_KEY is the API key for the Vision LLM
VISION_LLM_API_KEY = os.getenv("VISION_LLM_API_KEY", settings.vision_llm.api_key)

# VISION_LLM_MODEL is the model to use for the Vision LLM
VISION_LLM_MODEL = os.getenv("VISION_LLM_MODEL", settings.vision_llm.model_id)

# EMBEDDING_MODEL is the model to use for embeddings
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", settings.embedding.model_id)
