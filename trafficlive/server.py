import httplib, urllib, json, base64

class Server:
    """Wraps request/response."""

    DOMAIN_NAME = "api.sohnar.com"
    BASE_URL    = "/TrafficLiteServer/openapi"

    def __init__(self, email, token, page_size=50):
        self.email     = email
        self.token     = token
        self.page_size = page_size

    def get_employees(self, page=1):
        return self.__request(path="staff/employee", params={"currentPage": page})

    def get_employee(self, eid):
        return self.__request(path="staff/employee/%d" % (eid))

    def get_clients(self, page=1):
        return self.__request(path="crm/client", params={"currentPage": page})

    def get_jobs(self, page=1):
        return self.__request(path="job", params={"currentPage": page})

    def get_job(self, jid):
        return self.__request(path="job/%d" % (jid))

    def get_job_details(self, page=1):
        return self.__request(path="jobdetail", params={"currentPage": page})

    def get_job_detail(self, jdid):
        return self.__request(path="jobdetail/%d" % (jdid))


    def __request(self, method="GET", path="", params={}, headers={}):
        """Requests a resource from the server and returns the full response."""
        conn         = httplib.HTTPSConnection(self.DOMAIN_NAME)
        full_path    = "/".join([self.BASE_URL, path])
        full_params  = {"windowSize": self.page_size}
        full_headers = {
          "Authorization": self.__encode_credentials(),
          "Host": self.DOMAIN_NAME,
          "X-Target-URI": "https://" + self.DOMAIN_NAME,
          "Accept": "application/json",
          "Connection": "Keep-Alive"}

        full_params.update(params)
        full_headers.update(headers)
        full_params = urllib.urlencode(full_params)

        conn.request(method, full_path, full_params, full_headers)

        try:
            response = conn.getresponse()

            if response.status != 200:
                raise RuntimeError("Unexpected HTTP response: %s %s" % (response.status, response.reason))

            response = self.__wrap_response(response)
        finally:
            conn.close()

        return response

    def __wrap_response(self, response):
        """Wraps an API response in a data structure that's a little nicer to work with."""
        return {"status": response.status,
                "body": json.loads(response.read())}

    def __encode_credentials(self):
        """BASE64 encodes authentication details for delivery over HTTP."""
        return "Basic " + base64.b64encode("%s:%s" % (self.email, self.token))
