import pytest
from src.config import Config
from src.utils.logger import setup_logging
from src.utils.redis_client import RedisClient

def test_config_loading():
    """测试配置加载。"""
    config = Config()
    assert config.websocket_host == "0.0.0.0"
    assert config.redis_data_key == "your_data_key"

def test_logging_setup():
    """测试日志设置。"""
    setup_logging()
    logger = logging.getLogger("websocket_server")
    assert logger.level == logging.INFO

@pytest.mark.asyncio
async def test_redis_client():
    """测试Redis客户端。"""
    config = Config()
    redis_client = RedisClient(config)
    redis = await redis_client.get_redis()
    assert redis is not None
    await redis_client.close()
