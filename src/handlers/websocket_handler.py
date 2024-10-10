import asyncio
import json
from websockets import WebSocketServerProtocol, ConnectionClosedError
from prometheus_client import Counter, Gauge
from utils.logger import logger
from utils.redis_client import RedisClient
from config import Config

# 定义 Prometheus 指标
CONNECTIONS = Gauge("websocket_connections", "Current number of WebSocket connections")
MESSAGES_SENT = Counter("websocket_messages_sent", "Number of WebSocket messages sent")

async def websocket_handler(
    websocket: WebSocketServerProtocol, path: str, redis_client: RedisClient, config: Config
):
    """处理 WebSocket 连接并持续发送数据。"""
    client_ip = websocket.remote_address[0]
    logger.info(f"New WebSocket connection from {client_ip}")
    CONNECTIONS.inc()
    
    try:
        while True:
            data = await redis_client.get_data()
            if data is not None:
                message = json.dumps({"value": data})
                try:
                    if websocket.open:  # 确保 WebSocket 是开放的
                        await websocket.send(message)
                        MESSAGES_SENT.inc()
                        logger.debug(f"Sent data to client {client_ip}: {message}")
                except ConnectionClosedError:
                    logger.debug(f"Connection closed while trying to send to {client_ip}. Exiting loop.")
                    break  # 退出循环以结束处理

            await asyncio.sleep(config.websocket_update_interval)
    except asyncio.CancelledError:
        logger.info(f"WebSocket connection cancelled for {client_ip}")
    except Exception as e:
        logger.error(f"Error handling WebSocket connection for {client_ip}: {str(e)}", exc_info=True)
    finally:
        CONNECTIONS.dec()
        try:
            await websocket.close()
        except Exception as e:
            logger.error(f"Error closing WebSocket for {client_ip}: {str(e)}")
        logger.info(f"WebSocket connection closed for {client_ip}")
