from datetime import date, timedelta, time, datetime
from typing import List


class Job:

    def __init__(self, c: int, e: List[int], d: date, st: time, hn: int):
        self.customer = c
        self.employees = e
        self.date = d
        self.start_time = st
        self.hours_number = hn
        self.end_time = self._get_end_time()

    def _get_end_time(self):
        dt = datetime.combine(self.date, self.start_time) + timedelta(
            hours=int(self.hours_number),
            minutes=int((self.hours_number % 1) * 60)
        )
        return dt.time()

