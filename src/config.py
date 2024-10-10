from utils.logger import  logger
import os
import yaml
from dotenv import load_dotenv

# 仅在 `DOCKER_ENV` 标志为 True 时加载 .env 文件
if os.getenv('DOCKER_ENV') == 'true':
    load_dotenv()  

class Config:
    """配置类，加载并存储配置项。"""

    def __init__(self, config_path: str = "config.yaml"):
        self.config_data = self.load_config(config_path)

        self.websocket_host = os.getenv("WEBSOCKET_HOST", self.config_data["websocket"]["host"])
        self.websocket_port = int(os.getenv("WEBSOCKET_PORT", self.config_data["websocket"]["port"]))
        self.websocket_max_size = self.config_data["websocket"]["max_size"]
        self.websocket_max_queue = self.config_data["websocket"]["max_queue"]
        self.websocket_read_limit = self.config_data["websocket"]["read_limit"]
        self.websocket_write_limit = self.config_data["websocket"]["write_limit"]
        self.websocket_update_interval = self.config_data["websocket"]["update_interval"]

        self.redis_max_connections = self.config_data["redis"]["max_connections"]
        self.redis_encoding = self.config_data["redis"]["encoding"]
        self.redis_decode_responses = self.config_data["redis"]["decode_responses"]
        self.redis_data_key = self.config_data["redis"]["data_key"]
        self.redis_host = os.getenv('REDIS_HOST', self.config_data["redis"]["host"])
        logger.info(f"使用的Redis主机: {self.redis_host}")
        self.redis_port = os.getenv('REDIS_PORT', self.config_data["redis"]["port"])
        logger.info(f"使用的Redis端口: {self.redis_port}")
        self.redis_url = os.getenv('REDIS_URL', 'redis://' + self.redis_host + ':' + str(self.redis_port) + '/0')
        logger.info(f"使用的Redis URL: {self.redis_url}")

        self.prometheus_port = self.config_data["prometheus"]["port"]

    @staticmethod
    def load_config(config_path: str) -> dict:
        """加载配置文件。"""
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                config = yaml.safe_load(f)
            return config
        except FileNotFoundError as e:
            raise FileNotFoundError(f"配置文件未找到: {config_path}") from e
        except yaml.YAMLError as e:
            raise Exception(f"解析配置文件失败: {config_path}") from e
