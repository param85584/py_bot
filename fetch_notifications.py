from stackapi import StackAPI
import os
from dotenv import load_dotenv #this module is used to get the environment variables if it is set in a separate file like .env

load_dotenv() #access the variables from .env file. It accepts the path of .env file as it's arguments. If this file is in the current directory then no need to pass any argument. 

SITE = StackAPI('stackoverflow')

SITE.key=os.getenv('STACKOVERFLOW_KEY') #set the app key.
SITE.access_token=os.getenv('STACKOVERFLOW_TOKEN')
user_id=int(os.getenv('STACKOVERFLOW_USER_ID')) #convert the string value to integer using int function 

user_notifications = SITE.fetch('users/{ids}/notifications', ids=[user_id]) #it will store the notifications and other information in the dictionary form.

user_notify_msg=[] #initalise to store notification message having type and body of notification.

for i in range(len(user_notifications['items'])):
    b={'type': None , 'text': None} #initialize the value of type and text to None for each index of list 'user_notify_msg' 
    if 'body' in user_notifications['items'][i].keys():
        b['type']=user_notifications['items'][i]['notification_type']
        b['text']=user_notifications['items'][i]['body']
        user_notify_msg.append(b)
    else:
        b['type']=user_notifications['items'][i]['notification_type']
        user_notify_msg.append(b)

def stack_notify_msg():
    return user_notify_msg
