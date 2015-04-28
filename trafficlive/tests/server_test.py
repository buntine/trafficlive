from unittest import TestCase
import trafficlive.traffic_live as tl
import datetime as dt
import sys, os, json

# ACHTUNG!!
# You should copy/paste trafficlive/tests/data.json.example to traffilive/tests/data.json and fill
# out with real data for these tests to run successfully.

class TestServer(TestCase):
    def credentials(self):
        data = open(os.path.join(os.path.dirname(__file__), "data.json"), "r")
        parsed = json.load(data)

        data.close()

        return parsed

    def init_for(self, d):
        return (d["email"], d["token"], d["page_size"])

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
        s = tl.TrafficLive(*self.init_for(c))
        e = s.get_employees()
        b = e["body"]

        self.assertTrue(e["status"] == 200)
        self.assertTrue(len(b["resultList"]) > 1)
        self.assertTrue(b["resultList"][0]["userName"] != None)

    def test_get_employee(self):
        c = self.credentials()
        s = tl.TrafficLive(*self.init_for(c))
        e = s.get_employee(c["employee_id"])
        b = e["body"]

        self.assertTrue(e["status"] == 200)
        self.assertTrue(b["id"] == c["employee_id"])

#    def test_get_clients(self):
#        c = self.credentials()
#        s = tl.TrafficLive(*self.init_for(c))
#        e = s.get_clients()
#        b = e["body"]
#
#        self.assertTrue(e["status"] == 200)
#        self.assertTrue(len(b["resultList"]) > 1)
#        self.assertTrue(b["resultList"][0]["name"] != None)
#
#    def test_get_jobs(self):
#        c = self.credentials()
#        s = tl.TrafficLive(*self.init_for(c))
#        e = s.get_jobs()
#        b = e["body"]
#
#        self.assertTrue(e["status"] == 200)
#        self.assertTrue(len(b["resultList"]) > 1)
#        self.assertTrue(b["resultList"][0]["jobNumber"] != None)
#
#    def test_get_job(self):
#        c = self.credentials()
#        s = tl.TrafficLive(*self.init_for(c))
#        e = s.get_job(c["job_id"])
#        b = e["body"]
#
#        self.assertTrue(e["status"] == 200)
#        self.assertTrue(b["id"] == c["job_id"])
#
#    def test_get_job_details(self):
#        c = self.credentials()
#        s = tl.TrafficLive(*self.init_for(c))
#        e = s.get_job_details()
#        b = e["body"]
#
#        self.assertTrue(e["status"] == 200)
#        self.assertTrue(len(b["resultList"]) > 1)
#        self.assertTrue(b["resultList"][0]["name"] != None)
#
#    def test_get_time_entries(self):
#        c = self.credentials()
#        s = tl.TrafficLive(*self.init_for(c))
#        y = dt.timedelta(days=1)
#        sd = dt.date.today() - y - y
#        sd = sd.strftime("%Y-%m-%d")
#        ed = (dt.date.today() - y).strftime("%Y-%m-%d")
#        te = s.get_time_entries(sd, ed, c["employee_id"])
#        b = te["body"]
#
#        self.assertTrue(te["status"] == 200)
#        self.assertTrue(len(b["resultList"]) > 1)
#        self.assertTrue(b["resultList"][0]["minutes"] > 0)
#
    def test_add_time_entry(self):
        c = self.credentials()
        s = tl.TrafficLive(*self.init_for(c))
        td = dt.timedelta(minutes=120)
        st = dt.datetime.now() - td
        et = dt.datetime.now()
        te = s.add_time_entry({"trafficEmployeeId": c["employee_id"],
               "startTime": st.isoformat(),
               "endTime": et.isoformat(),
               "comment": "This is a test",
               "jobId/id": 111,
               "jobTaskId/id": 111,
               "billable": False,
               "minutes": 120})

        b = te["body"]

        self.assertTrue(te["status"] == 200)
        self.assertTrue(b["minutes"] == 120)

#    def test_get_job_task_allocations(self):
#        c = self.credentials()
#        s = tl.TrafficLive(*self.init_for(c))
#        e = s.get_job_task_allocations(c["employee_id"])
#        b = e["body"]
#
#        self.assertTrue(e["status"] == 200)
#        self.assertTrue(len(b["resultList"]) > 1)
#        self.assertTrue(b["resultList"][0]["taskDescription"] != None)
#
#    def test_get_calendar_block_allocations(self):
#        c = self.credentials()
#        s = tl.TrafficLive(*self.init_for(c))
#        e = s.get_calendar_block_allocations(c["employee_id"])
#        b = e["body"]
#
#        self.assertTrue(e["status"] == 200)
#        self.assertTrue(len(b["resultList"]) > 1)
#        self.assertTrue(b["resultList"][0]["trafficEmployeeId"] == c["employee_id"])
