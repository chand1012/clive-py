import os

from dotenv import load_dotenv

load_dotenv()

# LLM_BASE_URL is the base URL for the LLM
# If none is specified assume local Ollama
LLM_BASE_URL = os.getenv("LLM_BASE_URL", "http://localhost:11434")

# LLM_API_KEY is the API key for the LLM
LLM_API_KEY = os.getenv("LLM_API_KEY", "ollama")

# LLM_MODEL is the model to use for the LLM
# if none specified assume Gemma 3 12b
LLM_MODEL = os.getenv("LLM_MODEL", "ollama/gemma3:12b")

# VISION_LLM_BASE_URL is the base URL for the Vision LLM
VISION_LLM_BASE_URL = os.getenv(
    "VISION_LLM_BASE_URL", "http://localhost:11434")

# VISION_LLM_API_KEY is the API key for the Vision LLM
VISION_LLM_API_KEY = os.getenv("VISION_LLM_API_KEY", "ollama")

# VISION_LLM_MODEL is the model to use for the Vision LLM
VISION_LLM_MODEL = os.getenv("VISION_LLM_MODEL", "ollama/gemma3:12b")
