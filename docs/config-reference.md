# Config Reference:

## Table of Contents:

<!-- TOC -->

* [Config Reference:](#config-reference)
    * [Table of Contents:](#table-of-contents)
    * [About:](#about)
    * [Types Guide:](#types-guide)
    * [Setting/Config Guide:](#settingconfig-guide)

<!-- TOC -->

## About:

Here you will find a guide to what each setting that the bot comes with by default is for,
how it works, what you can set it to.

All values in the setting row can be altered with the /setting command.

> Ex. <br>
> `/setting set apod_channel 2345238457`

## Types Guide:

These are an explanation of types used in the config:

| Type         | Example                            | Notes                                           |
|--------------|------------------------------------|-------------------------------------------------|
| int          | `1`, `20`, `53`, `234`             | Must be a whole number.                         |
| float        | `1.5`, `23.454`, `213.23`, `3.005` | Numbers that contain a decimal.                 |
| string       | `asfd`, `Hello`                    | A set of characters, think words and sentences. |
| char         | `a`, `A`, `f`, `F`                 | A singular letter.                              |
| special_char | `!`, `@`, `#`, `$`, `%`            | Special characters that are not letter.         |
| NONE         | `NONE`                             | This is a value that can not be set.            |

## Setting/Config Guide:

| Setting                       | Allowed Values | Notes                                                                                 |
|-------------------------------|----------------|---------------------------------------------------------------------------------------|
| apod_channel                  | int            | Sets the channel where the daily apod post will happen.                               |
| apod_url                      | string         | The url from where to pull the daily image.                                           |
| guild                         | int            | The id of the server in which the bot will be used. Needed to sync commands           |
| prefix                        | special_char   | The prefix to use when running commands without the slash.                            |
| time                          | NONE           | See [hour](#hour) and [minute](#minute) values of this table for info on time values. |
| <span id=hour>hour</span>     | int            | The hour at which the bot will post in UTC time.                                      |
| <span id=minute>minute</span> | int            | The minute at which the bot will post in UTC time.                                    |
| token                         | string         | The token from the discord developer portal that is used to run and login the bot.    |
