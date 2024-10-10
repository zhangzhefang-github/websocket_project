import asyncio
from websockets import serve
from prometheus_client import start_http_server
from handlers.websocket_handler import websocket_handler
from utils.logger import setup_logging, logger
from config import Config
from utils.redis_client import RedisClient

async def main():
    """
    主函数：设置日志，加载配置，创建Redis连接池，启动WebSocket服务器。
    
    1. 设置日志记录。
    2. 加载配置文件。
    3. 创建Redis连接池。
    4. 启动Prometheus指标服务器。
    5. 启动WebSocket服务器。
    """
    setup_logging()
    logger.info("Initializing configuration")
    config = Config()
    logger.info(f"Configuration loaded: {config}, at line: {__import__('inspect').currentframe().f_lineno}")

    # 使用RedisClient类创建连接池，而不是直接使用Redis 
    redis_client = RedisClient(config)

    async with serve(
        lambda ws, path: websocket_handler(ws, path, redis_client, config),
        config.websocket_host,
        config.websocket_port,
        max_size=config.websocket_max_size,
        max_queue=config.websocket_max_queue,
        read_limit=config.websocket_read_limit,
        write_limit=config.websocket_write_limit,
    ):
        logger.info(f"WebSocket server started on {config.websocket_host}:{config.websocket_port}")
        await asyncio.Future()  # 运行直到手动停止

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        logger.critical(f"WebSocket server encountered a critical error: {str(e)}", exc_info=True)
