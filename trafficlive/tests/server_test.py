from unittest import TestCase
import trafficlive.traffic_live as tl
import datetime as dt
import sys

# You should have a file called ./auth in the root directory of this repo of the format:
#
# email@address,APITOKEN

class TestServer(TestCase):
    def credentials(self, page_size=2):
        details = open("auth", "r")
        creds   = details.read().rstrip("\n").split(",")

        creds.append(page_size)
        details.close()

        return creds

    def test_has_attributes(self):
        s = tl.TrafficLive("bunts@bunts.com", "abcd1234", 2)
        self.assertTrue(s.email == "bunts@bunts.com")
        self.assertTrue(s.token == "abcd1234")
        self.assertTrue(s.page_size == 2)

    def test_wrong_credentials(self):
        s = tl.TrafficLive("bunts@bunts.com", "abcd1234")

        with self.assertRaises(RuntimeError):
            s.get_employees()

    def test_get_employees(self):
        c = self.credentials()
        s = tl.TrafficLive(*c)
        e = s.get_employees()
        b = e["body"]

        self.assertTrue(e["status"] == 200)
        self.assertTrue(len(b["resultList"]) > 1)
        self.assertTrue(b["resultList"][0]["userName"] != None)
#
#    def test_get_employee(self):
#        c = self.credentials()
#        s = tl.TrafficLive(*c)
#        e = s.get_employee(39178)
#        b = e["body"]
#
#        self.assertTrue(e["status"] == 200)
#        self.assertTrue(b["id"] == 39178)
#
#    def test_get_clients(self):
#        c = self.credentials()
#        s = tl.TrafficLive(*c)
#        e = s.get_clients()
#        b = e["body"]
#
#        self.assertTrue(e["status"] == 200)
#        self.assertTrue(len(b["resultList"]) > 1)
#        self.assertTrue(b["resultList"][0]["name"] != None)
#
#    def test_get_jobs(self):
#        c = self.credentials()
#        s = tl.TrafficLive(*c)
#        e = s.get_jobs()
#        b = e["body"]
#
#        self.assertTrue(e["status"] == 200)
#        self.assertTrue(len(b["resultList"]) > 1)
#        self.assertTrue(b["resultList"][0]["jobNumber"] != None)
#
#    def test_get_job(self):
#        c = self.credentials()
#        s = tl.TrafficLive(*c)
#        e = s.get_job(905285)
#        b = e["body"]
#
#        self.assertTrue(e["status"] == 200)
#        self.assertTrue(b["id"] == 905285)
#
#    def test_get_job_details(self):
#        c = self.credentials()
#        s = tl.TrafficLive(*c)
#        e = s.get_job_details()
#        b = e["body"]
#
#        self.assertTrue(e["status"] == 200)
#        self.assertTrue(len(b["resultList"]) > 1)
#        self.assertTrue(b["resultList"][0]["name"] != None)
#
#    def test_get_time_entries(self):
#        c = self.credentials()
#        s = tl.TrafficLive(*c)
#        y = dt.timedelta(days=1)
#        sd = dt.date.today() - y - y
#        sd = sd.strftime("%Y-%m-%d")
#        ed = (dt.date.today() - y).strftime("%Y-%m-%d")
#        te = s.get_time_entries(sd, ed, 39178)
#        b = te["body"]
#
#        self.assertTrue(te["status"] == 200)
#        self.assertTrue(len(b["resultList"]) > 1)
#        self.assertTrue(b["resultList"][0]["minutes"] > 0)
#
#    def test_add_time_entry(self):
#        c = self.credentials()
#        s = tl.TrafficLive(*c)
#        td = dt.timedelta(minutes=120)
#        st = td.datetime.now() - td
#        te = s.add_time_entry(employee_id=39178,
#               start_time=st,
#               comment="This is a test",
#               job_id=111,
#               job_task_id=111,
#               billable=False,
#               minutes=120)
#        b = te["body"]
#
#        self.assertTrue(te["status"] == 200)
#        self.assertTrue(b["resultList"][0]["minutes"] == 120)
#
#    def test_get_job_task_allocations(self):
#        c = self.credentials()
#        s = tl.TrafficLive(*c)
#        e = s.get_job_task_allocations(39178)
#        b = e["body"]
#
#        self.assertTrue(e["status"] == 200)
#        self.assertTrue(len(b["resultList"]) > 1)
#        self.assertTrue(b["resultList"][0]["taskDescription"] != None)
#
#    def test_get_calendar_block_allocations(self):
#        c = self.credentials()
#        s = tl.TrafficLive(*c)
#        e = s.get_calendar_block_allocations(39178)
#        b = e["body"]
#
#        self.assertTrue(e["status"] == 200)
#        self.assertTrue(len(b["resultList"]) > 1)
#        self.assertTrue(b["resultList"][0]["trafficEmployeeId"] != None)
