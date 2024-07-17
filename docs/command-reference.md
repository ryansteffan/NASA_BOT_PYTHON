# Command Reference Guide:

## Table of Contents:

<!-- TOC -->

* [Command Reference Guide:](#command-reference-guide)
    * [Table of Contents:](#table-of-contents)
    * [Syntax conventions:](#syntax-conventions)
    * [Commands:](#commands)
        * [apod:](#apod)
            * [/daily_image](#daily_image)
        * [Built-In:](#built-in)
            * [/core_reload](#core_reload)
            * [/list_extensions](#list_extensions)
            * [/load_extension [_extension_]](#load_extension-extension)
            * [/reload_extension [_extension_]](#reload_extension-extension)
            * [/unload_extension [_extension_]](#unload_extension-extension)
            * [/sync](#sync)
        * [ping:](#ping)
            * [/ping {**True** OR **False**}](#ping-true-or-false)
        * [settings:](#settings)
            * [/setting list_all](#setting-list_all)
            * [/setting **set** {_setting_} {_new\_value_}](#setting-set-setting-new_value)
            * [/setting **unset** {_setting_}](#setting-unset-setting)
            * [/setting **restore** {_change\_number_}](#setting-restore-change_number)
            * [/setting **view_history**](#setting-view_history)

<!-- TOC -->

## Syntax conventions:

When reading the commands some of the syntax might be a bit confusing. To help here is a short guide
to the conventions that will be followed for all commands on this page.

| Syntax Item          | Explanation                                                                        |
|----------------------|------------------------------------------------------------------------------------|
| /command             | The name of a command, prefixed with a slash to indicate it is a slash command.    | 
| **sub_command**      | An argument used to alter the usage of the command.                                |  
| [_argument_]         | Indicates a command that is optional and the user must own input.                  |                
| {_arg1_ OR **arg2**} | Indicates the user must provide some form of input.                                |
| _italicized_         | If an argument is italicized that means the user chooses the input.                | 
| **bolded**           | If an argument is bolded, that means that the user must choose a predefined input. |

If you do not fully understand this right now, that is fine. You will learn to use the commands with time
and get used to them.

Finally, each command is organized by extension.

## Commands:

___

### apod:

___

#### /daily_image

Posts the Astronomy picture of the day. Post in channel the command is used in.

Required Permissions: None
___

### Built-In:

___

> :information_source: All the Built-In commands are core to the bot and
> can not be loaded/unloaded. They also are all hybrid commands
> (work with prefix and slash) to ensue that they always function. :information_source:
___

#### /core_reload

Fully restarts the discord bot.

Required Permissions: Administrator
___

#### /list_extensions

Lists all the extensions that are available to the bot.

Required Permissions: Administrator
___

#### /load_extension [_extension_]

Loads a specified extension. If no extension is specified then all available extensions are loaded.

Args:<br>
&emsp; extension: The name of the extension to load.

Required Permissions: Administrator
___

#### /reload_extension [_extension_]

Unloads and then loads an extension. If no extension is specified then all extensions are reloaded.

Args:<br>
&emsp; extension: The extension to reload.

Required Permissions: Administrator
___

#### /unload_extension [_extension_]

Unloads an extension. If no extension is specified all extensions are unloaded.

Args: <br>
&emsp; extension: The extension to unload.

Required Permissions: Administrator
___

#### /sync

Syncs the slash commands from the bot to the server.

Required Permissions: Administrator
___

### ping:

___

#### /ping {**True** OR **False**}

Checks the bot latency and test if it is up.

Args:<br>
&emsp; **True** OR **False**: If the bot should respond with the ping value.

Required Permissions: None
___

### settings:

___

#### /setting list_all

Lists all the settings that are currently configured for the bot.

Required Permissions: Administrator
___

#### /setting **set** {_setting_} {_new\_value_}

Updates a value in the bot config.

Args:<br>
&emsp; setting: The setting to make changes to.<br>
&emsp; new_value: The new value that the setting should be set to.

Required Permissions: Administrator
___

#### /setting **unset** {_setting_}

Sets a setting to the value of "unset".

Args:<br>
&emsp; setting: The setting that you want to set to a value of "unset".

Notes:<br>
You will probably almost never need to use this. The value that it sets the specified setting to
is a string value of unset. All this is useful for is if an extension wants to check if a value is unset.

Required Permissions: Administrator
___

#### /setting **restore** {_change\_number_}

Undoes a specified change from the command setting history.

Args:<br>
&emsp; change_number: The number of a change made. Found by using [/setting **view_history**](#setting-view_history).

Required Permissions: Administrator
___

#### /setting **view_history**

Lists the past 5 changes made the bot's config file.

Required Permissions: Administrator
___

