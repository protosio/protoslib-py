import requests

class Protos(object):
    """
    Implements a Protos client for the internal API
    """

    def __init__(self, appid, url='protos'):
        self.appid = appid
        self.url = url

    def get_domain(self):
        r = requests.get(self.url + 'internal/info/domain')
        info = r.json()
        return info['Domain']
