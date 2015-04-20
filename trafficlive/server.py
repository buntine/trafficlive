import httplib, base64

class Server:
    """Wraps request/response."""

    def __init__(self, email, token):
        self.email = email
	self.token = token

    def ping(self):
        return True

    def __request():
        pass
