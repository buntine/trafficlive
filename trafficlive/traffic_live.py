import trafficlive.server as tls

class TrafficLive(tls.Server):
    """."""

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

    def get_time_entries(self, start_date, end_date, employee_id=None):
        query = {
          "startDate": start_date,
          "endDate": end_date}

        if employee_id:
            query["filter"] = "trafficEmployeeId|EQ|%d" % (employee_id)

        return self._request(path="timeentries", query=query)

    def add_time_entry(employee_id=None, start_time=None, comment="", job_id=None, job_task_id=None, billable=False, minutes=0):
        pass

    def get_job_task_allocations(self, employee_id, page=1):
        path = "staff/employee/%s/jobtaskallocations" % (str(employee_id))
        return self._request(path=path, query={"currentPage": page})

    def get_calendar_block_allocations(self, employee_id, page=1):
        path = "staff/employee/%s/calendarblockallocations" % (str(employee_id))
        return self._request(path=path, query={"currentPage": page})