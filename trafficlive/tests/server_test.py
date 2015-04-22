from unittest import TestCase
from trafficlive import server as tls
import sys

class TestServer(TestCase):
    def test_has_attributes(self):
        print sys.argv[1]
        s = tls.Server("bunts@bunts.com", "abcd1234")
        self.assertTrue(s.email == "bunts@bunts.com")

    def test_wrong_credentials(self):
        s = tls.Server("bunts@bunts.com", "abcd1234")

        with self.assertRaises(RuntimeError):
            s.get_employees()
