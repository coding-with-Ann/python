import os 

BASE_URL = 'https://api.freeapi.app/'
BASE_PATH = 'api/'
VERSION = 'v1/'
USERS = 'kitchen-sink/'
METHOD = 'http-methods/'
REQUEST = 'post'


def users():
    return BASE_URL+BASE_PATH+VERSION+USERS+METHOD+REQUEST 


def access_token():
    return os.getenv('TEST_TOKEN')



    # access_token is exported to system instead of storing in code. 
    # This is done to protect the access token from unauthorized acceess. To export test token use this command in terminal
    # export TEST_TOKEN=1dhheuh777388
    # To see this test token use printenv token_name in terminal



