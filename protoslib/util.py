import os
from . import exceptions

def get_app_id():
    appid = os.environ.get('APPID')
    if not appid:
        raise exceptions.ProtosException('The APPID environment variable is empty or does not exist')
    return appid
