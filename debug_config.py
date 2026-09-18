#!/usr/bin/env python3
"""测试配置加载的调试脚本"""

from config import settings
import json


def test_config():
    """测试并打印当前配置信息"""
    print("=" * 60)
    print("配置加载测试")
    print("=" * 60)
    
    print(f"\n当前模型提供商: {settings.MODEL_PROVIDER}")
    print(f"温度参数: {settings.TEMPERATURE}")
    print(f"最大 Token 数: {settings.MAX_TOKENS}")
    
    print("\n--- 所有模型配置 ---")
    for provider, config in settings.models.items():
        print(f"\n{provider.upper()}:")
        print(f"  API Key: {config.api_key[:20]}..." if config.api_key else f"  API Key: (未配置)")
        print(f"  Base URL: {config.base_url}")
        print(f"  Model Name: {config.model_name}")
    
    print("\n--- 当前使用的模型配置 ---")
    try:
        current_config = settings.llm_config
        print(f"API Key: {current_config['api_key'][:20]}..." if current_config['api_key'] else "API Key: (未配置)")
        print(f"Base URL: {current_config['base_url']}")
        print(f"Model Name: {current_config['model_name']}")
        print("\n✅ 配置加载成功！")
    except Exception as e:
        print(f"\n❌ 配置加载失败: {e}")
        return False
    
    return True


if __name__ == "__main__":
    test_config()
