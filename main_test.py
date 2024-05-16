import logging
import logging.config

import yaml


def main():
    with (open("./conf/logging_config.yaml", 'r') as logging_config):
        config_data = yaml.safe_load(logging_config)
        print(config_data)
        logging.config.dictConfig(config_data)

        nasa_bot_logger = logging.getLogger("nasa_bot")
        print(nasa_bot_logger.name)

if __name__ == '__main__':
    main()
