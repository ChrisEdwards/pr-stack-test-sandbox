from logging import log_info

LOG_LEVEL = "INFO"

def configure_logging(level):
    global LOG_LEVEL
    LOG_LEVEL = level
    log_info(f"Log level set to {level}")
