from smolagents import LiteLLMModel

from src.utils.env import LLM_MODEL, LLM_BASE_URL, LLM_API_KEY
from src.utils.env import VISION_LLM_BASE_URL, VISION_LLM_API_KEY, VISION_LLM_MODEL

vision_model = LiteLLMModel(model_id=VISION_LLM_MODEL,
                            api_base=VISION_LLM_BASE_URL,
                            api_key=VISION_LLM_API_KEY)

llm_model = LiteLLMModel(model_id=LLM_MODEL,
                         api_base=LLM_BASE_URL,
                         api_key=LLM_API_KEY)
