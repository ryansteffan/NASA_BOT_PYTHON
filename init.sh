#!/usr/bin/env bash

# Used to set initial config values and start the bot.

echo "The prefix is set to: $prefix";
echo "The guild is set to: $guild";
echo "The token is set to: $token";

echo "prefix: \"$prefix\"" >> ./conf/config.yaml;
echo "guild: \"$guild\"" >> ./conf/config.yaml;
echo "token: \"$token\"" >> ./conf/config.yaml;

/usr/bin/supervisord
