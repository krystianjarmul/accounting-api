from datetime import date, time

from src import model


def test_job_counts_end_time_based_on_hours_and_start_time():
    job1 = model.Job(1, 1, date(2011, 11, 11), time(11, 30), 2)
    job2 = model.Job(1, 1, date(2011, 11, 11), time(11, 30), 2.5)
    job3 = model.Job(1, 1, date(2011, 11, 11), time(11, 00), 2.5)
    assert job1.end_time == time(13, 30)
    assert job2.end_time == time(14, 00)
    assert job3.end_time == time(13, 30)

