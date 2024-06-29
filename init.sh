#!/bin/bash

# Used to set initial config values and start the bot.

current_prefix=$(awk '/prefix/ {print $1}' conf/bot_config.yaml);
current_guild=$(awk '/guild/ {print $1}' conf/bot_config.yaml);
current_token=$(awk '/token/ {print $1}' conf/bot_config.yaml);

if [ "$current_prefix" == "" ] && [ "$current_guild" == "" ] && [ "$current_token" == "" ]; then
  echo "prefix: \"$prefix\"" >> ./conf/bot_config.yaml;
  echo "guild: \"$guild\"" >> ./conf/bot_config.yaml;
  echo "token: \"$token\"" >> ./conf/bot_config.yaml;
  echo "Set up has completed!";
else
  echo "Config already set, skipping setup...";
fi

/usr/bin/supervisord;