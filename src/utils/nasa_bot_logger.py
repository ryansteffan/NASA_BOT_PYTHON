import logging
from logging.config import dictConfig

import yaml

"""
A simple library that loads the logging config used by nasa bot
"""

try:
    with open("./conf/logging_config.yaml", 'r') as logging_config:
        config_data = yaml.safe_load(logging_config)
        logging.config.dictConfig(config_data)
except Exception as e:
    print(f"An exception has taken place while "
          f"configuring nasa_bot's logging: {e}")

nasa_bot_logger = logging.getLogger("nasa_bot")
"""
The logger that is used by all of nasa bot.
"""
