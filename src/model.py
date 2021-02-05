from datetime import date, timedelta, time, datetime
from typing import List


class Job:

    def __init__(self, c: int, e: List[int], d: date, st: time, hn: int):
        self.customer = c
        self._employees = e
        self.date = d
        self.start_time = st
        self.hours_number = hn
        self.end_time = self._get_end_time()
        self.employees = self._employees_to_string()
        self.reference = self._get_reference()

    def _get_end_time(self):
        dt = datetime.combine(self.date, self.start_time) + timedelta(
            hours=int(self.hours_number),
            minutes=int((self.hours_number % 1) * 60)
        )
        return dt.time()

    def _employees_to_string(self):
        if isinstance(self._employees, str):
            return self._employees
        return ','.join([str(e) for e in self._employees])

    def _get_reference(self):
        only_digits_date = str(self.date).replace('-', '')
        employees_ids_connected = ''.join([str(e) for e in self._employees])
        return str(self.customer) + employees_ids_connected + only_digits_date

    def __hash__(self):
        return hash(self.reference)

    def __eq__(self, other):
        if not isinstance(other, Job):
            return False
        return other.reference == self.reference
# TODO separate test env from dev