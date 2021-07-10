from stackapi import StackAPI
import os
from dotenv import load_dotenv #this module is used to get the environment variables if it is set in a separate file like .env

load_dotenv() #access the variables from .env file. It accepts the path of .env file as it's arguments. If this file is in the current directory then no need to pass any argument. 

SITE = StackAPI('stackoverflow')

SITE.key=os.getenv('STACKOVERFLOW_KEY') 
SITE.access_token=os.getenv('STACKOVERFLOW_TOKEN')
user_id=int(os.getenv('STACKOVERFLOW_USER_ID')) 

user_notifications = SITE.fetch('users/{ids}/notifications', ids=[user_id])

user_notify_type=[]
user_notify_msg=[]
a=[]

for index,value in enumerate(user_notifications['items']):

    if 'body' in value.keys():
        user_notify_type.append(user_notifications['items'][index]['notification_type'])
        user_notify_msg.append(user_notifications['items'][index]['body'])

    else:
        user_notify_type.append(user_notifications['items'][index]['notification_type'])

#print(user_notify_type)
print(user_notify_msg)

