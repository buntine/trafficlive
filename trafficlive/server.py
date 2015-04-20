import httplib, urllib, json, base64

class Server:
    """Wraps request/response."""

    DOMAIN_NAME = "api.sohnar.com"
    BASE_URL    = "/TrafficLiteServer/openapi"

    def __init__(self, email, token):
        self.email = email
        self.token = token

    def get_all_employess(self):
        return True

    def __request(self, method="GET", path="", params={}, headers={}):
        """Requests a resource from the server and returns the full response."""
        conn         = httplib.HTTPSConnection(DOMAIN_NAME)
        full_path    = "/".join([BASE_URL, path])
        full_params  = urllib.urlencode(params)
        full_headers = {
          "Authorization": self.__encode_credentials(),
          "X-Target-URI": DOMAIN_NAME,
          "Accept": "application/json",
          "Connection": "Keep-Alive"}
        full_headers.update(headers)

        conn.request(method, full_path, full_params, full_headers)
        response = conn.getresponse()
        conn.close()

        return response

    def __encode_credentials(self):
        """BASE64 encodes authentication details for delivery over HTTP."""
        base64.b64encode("Basic %s:%s" % (self.email, self.token))
