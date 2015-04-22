from unittest import TestCase
from trafficlive import server as tls
import sys

# You should have a file called ./auth in the root directory of this repo of the format:
#
# email@address,APITOKEN

class TestServer(TestCase):
    def credentials(self):
        details = open("auth", "r")
        return details.read().rstrip("\n").split(",")

    def test_has_attributes(self):
        s = tls.Server("bunts@bunts.com", "abcd1234")
        self.assertTrue(s.email == "bunts@bunts.com")

    def test_wrong_credentials(self):
        s = tls.Server("bunts@bunts.com", "abcd1234")

        with self.assertRaises(RuntimeError):
            s.get_employees()

    def test_get_employees(self):
        c = self.credentials()
        s = tls.Server(*c)
        e = s.get_employees()
        b = e["body"]

        self.assertTrue(e["status"] == 200)
        self.assertTrue(len(b["resultList"]) > 1)
        self.assertTrue(len(b["resultList"][0]["userName"]) != None)

    def test_get_employee(self):
        c = self.credentials()
        s = tls.Server(*c)
        e = s.get_employee(39178)
        b = e["body"]

        self.assertTrue(e["status"] == 200)
        self.assertTrue(b["id"] == 39178)
