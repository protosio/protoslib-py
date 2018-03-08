import os

class ProtosException(Exception):
    pass

def GetAppID():
    appid = os.environ.get('APPID')
    if not appid:
        raise ProtosException('The APPID environment variable is empty or does not exist')
    return appid