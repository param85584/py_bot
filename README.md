# py_bot

install a discord library
pip install -U discord.py
using this command

after that run the code 
then their our bot name will be 
and then type in $hello in a server
and then bot will reply the message

client.run('token')

check if the code is not working
then a new token is generated
which i will provide it to you....


This repository helps to send the stackoverflow notifications to Discord app as a message(real-time) using Python.

This project is divided in two tasks:
1. Fetch notifications from Stackoverflow using Stack Exchange API.
2. Send these notifications to Discord using Discord Bot in Python.

In order to fetch the notifications you need to authenticate your app. For more details read this https://api.stackexchange.com/docs/authentication

You can obtain your own app key from here https://stackapps.com/apps/oauth/register
By registering your application you will get various parameters like client_id, scope, redirect_uri and many more.

I used the implicit OAuth 2.0 flow consists of the following steps:

Open a new window at https://stackoverflow.com/oauth/dialog, with these query string parameters
client_id
scope (details)
redirect_uri - must be under an apps registered domain
state - optional
The user approves your app
The user is redirected to redirect_uri, with these parameters in the hash
access_token
expires - optional, only if scope doesn't contain no_expiry

Example: https://stackoverflow.com/oauth/dialog?client_id=12345&scope=read_inbox,no_expiry&redirect_uri=https://stackexchange.com/oauth/login_success

This request is responded to with either an error (HTTP status code 400) or an access token of the form access_token=...&expires=1234. expires will only be set if scope does not include no_expiry, the use of which is strongly advised against unless your app truly needs perpetual access.

Now by this, you have "app key", "access_token" and "user_id". We will use these three to fetch notifications. Since these are different person to person. Moreover all these variables are kept to be secret. So we will create a separate file .env and set the value to the variables.

2. Create a file .env of the format.

STACKOVERFLOW_KEY=''  #App key value
STACKOVERFLOW_TOKEN='' #Access_token
STACKOVERFLOW_USER_ID='' #user id. You can get it if you signed in stackoverflow

Put the values to these variables respectively.

