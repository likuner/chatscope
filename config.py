from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal, Dict


class ModelConfig(BaseModel):
    """Configuration for a specific LLM provider."""
    api_key: str = ""
    base_url: str
    model_name: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
        env_nested_delimiter="__"
    )
    
    # Model provider: qwen, deepseek, or glm
    MODEL_PROVIDER: Literal["qwen", "deepseek", "glm"] = "deepseek"
    
    # Qwen configuration
    QWEN_API_KEY: str = ""
    QWEN_BASE_URL: str = "https://dashscope.aliyuncs.com/compatible-mode/v1"
    QWEN_MODEL_NAME: str = "qwen-max"
    
    # DeepSeek configuration
    DEEPSEEK_API_KEY: str = ""
    DEEPSEEK_BASE_URL: str = "https://api.deepseek.com"
    DEEPSEEK_MODEL_NAME: str = "deepseek-chat"
    
    # GLM configuration
    GLM_API_KEY: str = ""
    GLM_BASE_URL: str = "https://open.bigmodel.cn/api/paas/v4"
    GLM_MODEL_NAME: str = "glm-4-plus"
    
    # Model parameters
    TEMPERATURE: float = 0.7
    MAX_TOKENS: int = 2048
    
    @property
    def models(self) -> Dict[str, ModelConfig]:
        """Get all model configurations as nested structure."""
        return {
            "qwen": ModelConfig(
                api_key=self.QWEN_API_KEY,
                base_url=self.QWEN_BASE_URL,
                model_name=self.QWEN_MODEL_NAME
            ),
            "deepseek": ModelConfig(
                api_key=self.DEEPSEEK_API_KEY,
                base_url=self.DEEPSEEK_BASE_URL,
                model_name=self.DEEPSEEK_MODEL_NAME
            ),
            "glm": ModelConfig(
                api_key=self.GLM_API_KEY,
                base_url=self.GLM_BASE_URL,
                model_name=self.GLM_MODEL_NAME
            )
        }
    
    @property
    def llm_config(self) -> Dict[str, str]:
        """Get configuration for the currently selected model provider."""
        model = self.models.get(self.MODEL_PROVIDER)
        if not model:
            raise ValueError(f"Unsupported model provider: {self.MODEL_PROVIDER}")
        
        return {
            "api_key": model.api_key,
            "base_url": model.base_url,
            "model_name": model.model_name,
        }


settings = Settings()
