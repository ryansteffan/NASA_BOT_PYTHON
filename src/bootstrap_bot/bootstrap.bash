#!/usr/bin/env bash

function restart_bot() {
  # Gets the PID of the bot.
  var=$( ps -ef | grep "python3 main.py" | grep -v grep | awk '{ print $2 }');
  kill $var;
  echo "The bot has been killed.";
  python3 main.py;
  echo "The bot has been started."
}

restart_bot;