To install and run the bot:

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

This is planned to be changed in the future and have a proper updater