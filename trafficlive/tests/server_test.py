from unittest import TestCase

from trafficlive import server as tls

class TestServer(TestCase):
    def test_has_attributes(self):
        s = tls.Server("bunts@bunts.com", "abcd1234")
        self.assertTrue(s.email == "bunts@bunts.com")

    def test_get_employees_works(self):
        s = tls.Server("bunts@bunts.com", "abcd1234")
        e = s.get_employees()

        self.assertTrue(e.status == 200)
        self.assertTrue(e.status == 200)
