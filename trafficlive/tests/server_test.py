from unittest import TestCase

from trafficlive import server as tls

class TestServer(TestCase):
    def test_has_attributes(self):
        s = tls.Server("bunts@bunts.com", "abcd1234")
        self.assertTrue(s.email == "bunts@bunts.com")
