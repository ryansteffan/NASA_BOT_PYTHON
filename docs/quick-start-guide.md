# How to get started:

## Table of Contents:

<!-- TOC -->

* [How to get started:](#how-to-get-started)
    * [Table of Contents:](#table-of-contents)
    * [Using Docker (Recommended):](#using-docker-recommended)
        * [What you will need before you get started:](#what-you-will-need-before-you-get-started)
        * [Break Down of the Run Command:](#break-down-of-the-run-command)
    * [Running on bare metal:](#running-on-bare-metal)
        * [supervisord:](#supervisord)
    * [Setting up in discord:](#setting-up-in-discord)
        * [Changing the NASA api key:](#changing-the-nasa-api-key)

<!-- TOC -->

## Using Docker (Recommended):

> :warning: This section assumes that you already have docker installed,
> if you do not, pause here and go install docker. Once you are done, continue here. :warning:

> Dockers Documentation: [https://docs.docker.com/](https://docs.docker.com/)

___

> :warning:This guide also assumes that you have created a bot using the discord developer
> portal, if you have not then pause here, and then continue here after that is done. :warning:

> How to create a discord
>
bot: [https://discordpy.readthedocs.io/en/stable/discord.html](https://discordpy.readthedocs.io/en/stable/discord.html)

___

#### What you will need before you get started:

- The token for your discord bot. Obtained from the discord developer portal.
- The guild of the server that you wish to invite the bot to. This can be obtained by using the dev tools in the discord
  app.
- Choose a prefix to use for the bot. If you are unsure what to choose, check what bots you have in your server, and see
  what they use. You do not want to have conflicts. Good options are special characters (!@#$%^&*) as they are not used
  to prefix messages usually.

Using Docker to deploy the bot is the easiest and best supported method. Below is the commands
needed to get started with it:

First pull the image:

```shell
docker pull ryansteffan/nasa_bot
```

Then run the container, here is a basic command to get it up and running:

```shell
docker run -d --name nasa_bot --restart always -e prefix={choose_a_prefix} -e guild={server_id} -e token={token_for_bot} ryansteffan/nasa_bot
```

#### Break Down of the Run Command:

- `--name` is used to name the bot, we are giving the bot the name nasa_bot in the example.
- `--restart always` tells the bot when to restart, always makes sure it starts on boot or if it crashes.
- `-e` is used to pass environment variables, prefix is the prefix for commands, guild is your server id, and the token
  is the token for the bot.

## Running on bare metal:

> :warning: Continue with caution, this form of deployment is missing features. :warning:

While it is possible, it is not recommended that you deploy using bare metal.
Some features are missing, and this form of deployment will see minimal development resources.

That being said, here are the basics to get it up and running:

First ensure that the needed dependencies are installed:

```shell
# On Debian/Ubuntu
sudo apt update
sudo apt upgrade
sudo apt install python3 python3-venv
```

```shell
# On Arch based Linux distros
sudo pacman -Syu
sudo pacman -S python3 python3-venv
```

Start by making a directory to store the bot in:

```shell
mkdir ./nasa_bot
cd ./nasa_bot
```

Then you will need to clone the GitHub repo into the folder:

```shell
git clone https://github.com/TheTurnnip/NASA_BOT_PYTHON.git
cd ./NASA_BOT_PYTHON
```

Make a virtual environment to install the bot in, and install the required packages:

```shell
python3 -m venv .
source ./bin/activate
pip install -r ./requirements.txt
```

Now configure the bot with the required settings to get it running:

```shell
# Using nano to edit the file. Press ctrl + x to exit and save.
nano ./conf/bot_config.yaml
```

Finally, run the bot:

```shell
python3 main.py
```

That is it, you now have a basic form of the bot running on bare metal.

You are probably going to want to run the bot in the background, this is beyond the scope
of the tutorial.

If you wish to do so, here are a few places to look to get you started:

- systemd (built into most linux distros).
- cron (Used to schedule tasks on linux, simpler than systemd).
- supervisord (Not included with most distros, see below for some details on it.)

#### supervisord:

Supervisor Documentation:

[http://supervisord.org/](http://supervisord.org/)

If you choose to use this, some of the work is done for you already and it will restore the lost functionality
of restarting the bot via discord commands.

First, you need to install supervisord.

Next, you will need to configure supervisord, which can be done with the supervisord.conf file in the GitHub repo.

And that is the basics. Make sure to read the docs for supervisord as this is a very cursory glance of it.

## Setting up in discord:

Now that the bot has been installed, a few tweaks need to be made in discord.

Here is a quick list of things to do:

1. Sync the app commands. By default, you will not have slash commands because they must sync.
   Refer to the [/sync](command-reference.md#sync) command for guidance.
2. Set the channel for nasa_bot to post images in. Refer to
   the [/setting](command-reference.md#setting-set-setting-new_value) command.
3. Set the time to post the image at (Time is in 24-hour format, and the timezone is UTC).
   Refer to the [/setting](command-reference.md#setting-set-setting-new_value) command for this as well.
4. I suggest that you get an API token from NASA's open api if you wish to use the bot extensively,
   as the demo key is great to get the bot up and running, but NASA suggests users use a normal key.
   Below are instructions on how to change the key.
5. Use the [/reload_extension](command-reference.md#reload_extension-extension) command
   (with no optional parameters) to reload all the extensions.

#### Changing the NASA api key:

To change the key, the easiest method is to onece again use the /setting command.
You are going to want to set the value of the apod_url. The value can be kept mostly the same
just change what the api_key is equal to.

Ex. Instead of `https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY` you could change the value to something like
`https://api.nasa.gov/planetary/apod?api_key=12345`, where 12345 is your nasa api key.

Now reload the extensions and test if the api key works with the /apod_daily command.

If the command does not work, you are going to want to roll back the changes. Take a look at the
[/setting restore](command-reference.md#setting-restore-change_number) command.