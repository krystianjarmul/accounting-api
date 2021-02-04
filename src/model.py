from datetime import date, timedelta, time
from typing import List


class Job:

    def __init__(self, c: int, e: List[int], d: date, st: time, hn: int):
        self.customer = c
        self.employees = e
        self.date = d
        self.start_time = st
        self.hours_number = hn
