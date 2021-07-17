from stackapi import StackAPI
import os
from dotenv import load_dotenv #this module is used to get the environment variables if it is set in a separate file like .env

load_dotenv() #access the variables from .env file. It accepts the path of .env file as it's arguments. If this file is in the current directory then no need to pass any argument. 

SITE = StackAPI('stackoverflow')

SITE.key=os.getenv('STACKOVERFLOW_KEY') #set the app key.
SITE.access_token=os.getenv('STACKOVERFLOW_TOKEN')
user_id=int(os.getenv('STACKOVERFLOW_USER_ID')) #convert the string value to integer using int function 

user_notifications = SITE.fetch('users/{ids}/notifications', ids=[user_id]) #it will store the notifications and other information in the dictionary form.

user_notify_type=[] #initialise to store type of notification   
user_notify_msg=[] #initalise to store notification message

#The value of key "items" of dictionary "user_notifications" is list. Each element of this list represents single notification and it's detail in  dictionary form.

for index,value in enumerate(user_notifications['items']): #index tell the index number of list "user_notifications['items']" and value represents the notification details of that index. The "value" is in the dictionary form.

    if 'body' in value.keys(): 
        user_notify_type.append(user_notifications['items'][index]['notification_type'])
        user_notify_msg.append(user_notifications['items'][index]['body'])

    else:
        user_notify_type.append(user_notifications['items'][index]['notification_type'])

#print(user_notify_type)
def stack_notify_msg():
    return user_notify_msg
