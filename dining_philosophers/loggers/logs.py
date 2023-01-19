import logging
import logging.config
import yaml

def config_logging(config_path):
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)