import httplib, urllib, json, base64

class Server:
    """Wraps request/response."""

    DOMAIN_NAME = "api.sohnar.com"
    BASE_URL    = "/TrafficLiteServer/openapi"

    def __init__(self, email, token):
        self.email = email
        self.token = token

    def get_employees(self):
        self.__request(path="staff/employee")

    def __request(self, method="GET", path="", params={}, headers={}):
        """Requests a resource from the server and returns the full response."""
        conn         = httplib.HTTPSConnection(self.DOMAIN_NAME)
        full_path    = "/".join([self.BASE_URL, path])
        full_params  = urllib.urlencode(params)
        full_headers = {
          "Authorization": self.__encode_credentials(),
          "X-Target-URI": self.DOMAIN_NAME,
          "Accept": "application/json",
          "Connection": "Keep-Alive"}
        full_headers.update(headers)

        conn.request(method, full_path, full_params, full_headers)

        try:
            response = conn.getresponse()

            if response.status != 200:
                raise RuntimeError("Received HTTP %s" % (response.status))
        finally:
            conn.close()

        return self.__wrap_response(response)

    def __wrap_response(self, response):
        """Wraps an API response in a data structure that's a little nicer to work with."""
        return {"status": response.status,
                "body": json.loads(response.read())}

    def __encode_credentials(self):
        """BASE64 encodes authentication details for delivery over HTTP."""
        return "Basic " + base64.b64encode("%s:%s" % (self.email, self.token))
