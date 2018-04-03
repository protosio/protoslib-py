from requests import Request, Session
from . import exceptions

class Protos(object):
    """
    Implements a Protos client for the internal API
    """

    def __init__(self, appid, url='http://protos:8080/'):
        self.appid = appid
        self.url = url

    def _send_request(self, req):
        req.headers = {'Appid': self.appid}
        req.url = self.url + req.url
        pre = req.prepare()
        s = Session()
        resp = s.send(pre)
        if resp.status_code == 401:
            raise exceptions.Unauthorized(resp.text.rstrip())
        if resp.status_code == 403:
            raise exceptions.Forbidden(resp.text.rstrip())
        if resp.status_code != 200:
            raise exceptions.ProtosException(resp.text.rstrip())
        return resp

    def get_domain(self):
        req = Request('GET', 'internal/info/domain')
        r = self._send_request(req)
        info = r.json()
        return info['domain']

    def get_app_info(self):
        req = Request('GET', 'internal/info/app')
        r = self._send_request(req)
        info = r.json()
        return info

    # Consumer methods
    def create_resource(self, resource):
        req = Request('POST', 'internal/resource', json=resource)
        r = self._send_request(req)
        return r.json()

    def get_resource(self, resourceID):
        req = Request('GET', 'internal/resource/' + resourceID)
        r = self._send_request(req)
        return r.json()

    def delete_resource(self, resourceID):
        req = Request('DELETE', 'internal/resource/' + resourceID)
        self._send_request(req)

    # Provider methods
    def register_provider(self, rtype):
        req = Request('POST', 'internal/provider/' + rtype)
        self._send_request(req)

    def deregister_provider(self, rtype):
        req = Request('DELETE', 'internal/provider/' + rtype)
        self._send_request(req)

    def authenticate_user(self, username, password):
        userdata = {'username': username, 'password': password}
        req = Request('POST', 'internal/user/auth', json=userdata)
        user = None
        try:
            user = self._send_request(req)
        except exceptions.Unauthorized:
            return user
        return user
