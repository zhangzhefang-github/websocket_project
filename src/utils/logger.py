import logging
import logging.config
import yaml

def setup_logging(logging_config_path: str = "logging_config.yaml"):
    """设置日志配置。"""
    try:
        with open(logging_config_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
            logging.config.dictConfig(config)
        logging.info("Logging configuration loaded successfully")
    except Exception as e:
        logging.basicConfig(level=logging.INFO)
        logging.error(f"Failed to load logging configuration: {str(e)}", exc_info=True)

# 获取默认的logger
logger = logging.getLogger("websocket_server")
