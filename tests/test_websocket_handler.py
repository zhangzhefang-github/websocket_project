import pytest
from unittest.mock import AsyncMock, patch
from src.handlers.websocket_handler import websocket_handler
from src.config import Config
from src.utils.redis_client import RedisClient

@pytest.mark.asyncio
async def test_websocket_handler():
    """测试WebSocket处理函数。"""
    websocket = AsyncMock()
    websocket.remote_address = ("127.0.0.1", 12345)
    path = "/test"
    config = Config()
    redis_client = AsyncMock(spec=RedisClient)
    redis_client.get_data.return_value = 42.0

    with patch("src.handlers.websocket_handler.CONNECTIONS") as mock_connections, \
         patch("src.handlers.websocket_handler.MESSAGES_SENT") as mock_messages_sent:

        mock_connections.inc = AsyncMock()
        mock_connections.dec = AsyncMock()
        mock_messages_sent.inc = AsyncMock()

        task = asyncio.create_task(websocket_handler(websocket, path, redis_client, config))

        await asyncio.sleep(0.1)  # 等待handler开始运行
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            pass

        websocket.send.assert_called_with('{"value": 42.0}')
        mock_connections.inc.assert_called_once()
        mock_connections.dec.assert_called_once()
        mock_messages_sent.inc.assert_called_once()
