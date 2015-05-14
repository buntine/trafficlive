import datetime as dt
import json
import trafficlive.server as tls

class TrafficLive(tls.Server):
    """Defines all public wrapper functions."""

    def get_employees(self, page=1):
        return self._request(path="staff/employee", query={"currentPage": page})

    def get_employee(self, eid):
        return self._request(path="staff/employee/%d" % (eid))

    def get_clients(self, page=1):
        return self._request(path="crm/client", query={"currentPage": page})

    def get_jobs(self, page=1):
        return self._request(path="job", query={"currentPage": page})

    def get_job(self, jid):
        return self._request(path="job/%d" % (jid))

    def get_job_details(self, page=1):
        return self._request(path="jobdetail", query={"currentPage": page})

    def get_job_detail(self, jdid):
        return self._request(path="jobdetail/%d" % (jdid))

    def get_charge_bands(self, page=1):
        return self._request(path="chargeband", query={"currentPage": page})

    def get_charge_band(self, cbid):
        return self._request(path="chargeband/%d" % (cbid))

    def get_time_entries(self, start_date, end_date, employee_id=None):
        query = {
          "startDate": start_date,
          "endDate": end_date}

        if employee_id:
            query["filter"] = "trafficEmployeeId|EQ|%d" % (employee_id)

        return self._request(path="timeentries", query=query)

    def add_time_entry(self, merge_values={}):
        headers     = {"Content-Type": "application/json"}
        full_values = {"dateCreated": dt.datetime.utcnow().isoformat()}

        full_values.update(merge_values)

        body = self._merge_into_template("time_entry", full_values)

        return self._request(path="timeentries", method="PUT", body=json.dumps(body), headers=headers)

    def get_job_task_allocations(self, employee_id, page=1):
        path = "staff/employee/%s/jobtaskallocations" % (str(employee_id))
        return self._request(path=path, query={"currentPage": page})

    def get_calendar_block_allocations(self, employee_id, page=1):
        path = "staff/employee/%s/calendarblockallocations" % (str(employee_id))
        return self._request(path=path, query={"currentPage": page})
