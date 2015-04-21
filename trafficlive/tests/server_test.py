from unittest import TestCase
from trafficlive import server as tls
import sys

class TestServer(TestCase):
    def test_has_attributes(self):
        print sys.argv[1]
        s = tls.Server("bunts@bunts.com", "abcd1234")
        self.assertTrue(s.email == "bunts@bunts.com")

    def test_get_employees_works(self):
        s = tls.Server("bunts@bunts.com", "abcd1234")
        e = s.get_employees()

        self.assertTrue(e["status"] == 200)
