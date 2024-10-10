import asyncio
from redis.asyncio import Redis
from config import Config
from utils.logger import logger

class RedisClient:
    """Redis客户端封装，管理连接和数据获取。"""

    def __init__(self, config: Config):
        self.config = config
        self.redis: Redis = None
        self.lock = asyncio.Lock()

    async def get_redis(self) -> Redis:
        """获取Redis连接实例，使用单例模式。"""
        async with self.lock:
            if self.redis is None:
                self.redis = Redis.from_url(
                    self.config.redis_url,
                    max_connections=self.config.redis_max_connections,
                    encoding=self.config.redis_encoding,
                    decode_responses=self.config.redis_decode_responses,
                )
                logger.info("Redis connection pool created")
            return self.redis

    async def get_data(self) -> float:
        """从Redis中获取数据。"""
        try:
            redis = await self.get_redis()
            value = await redis.get(self.config.redis_data_key)
            if value is not None:
                return float(value)
            else:
                logger.debug("No data found in Redis for key: {self.config.redis_data_key}")
                return None
        except Exception as e:
            logger.error(f"Error fetching data from Redis: {str(e)}", exc_info=True)
            return None

    async def close(self):
        """关闭Redis连接。"""
        if self.redis:
            await self.redis.close()
            logger.info("Redis connection closed")
