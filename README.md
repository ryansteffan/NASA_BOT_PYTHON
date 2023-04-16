<h1>To install and run the bot:</h1>

Docker is the perfered method of install but it is not the only option that is avaiable, those are discussed below.

<h2>To install via docker(Recommended):</h2>

1. Clone the repo with "git clone https://github.com/TheTurnnip/NASA_BOT_PYTHON.git"
2. Modifiy the config. Set the bot token, channel id, and the post time. MUST BE DONE BEFORE BUILDING IMAGE, AND TIME MUST BE UTC.
3. run, "docker build . -t nasa_bot", to build the docker image.
4. run "docker run nasa_bot" to start the bot.

If you wish to have the bot to start at server boot then add "--restart always" to the run command (ie. "docker run --restart always nasa_bot")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<h2>Bare metal(Depercated)</h2>

1. Copy the bot into the directory that you wish to install it in 
2. Navigate to the directory using cd
3. Run "pip install ." to install all of the needed dependencies and the NASA_API package that the bot uses.
4. Edit the "./conf/config.yaml" to contain a valid token obtained from the discord developer portal and set the channel id for the daily upload. DO NOT CHANGE THE URL, IT IS
    REQUIRED TO PULL INFO FROM THE NASA API.
5. Run the bot with "python ./main.py", this may require that you use python3 depending on OS/platform. In that case "python3 ./main.py" is the right syntax.
6. In order to update the bot:
    - Make a backup of the config in "./conf/config.yaml" and save it to some other location. 
    - Remove this directory ("NASA_BOT_PYTHON" is the default).
    - Copy the new version of the bot to where ever you wish it install it.
    - Repeat steps 2-5, but restore the old config by copying it to "./conf/config.yaml"

PREVIOUS PLAN TO HAVE AN UPDATER HAS SHIFTED TO FAVOUR DOCKER SUPPORT
