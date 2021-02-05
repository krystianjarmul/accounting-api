from datetime import date, time

from src import model


def test_job_counts_end_time_based_on_hours_and_start_time():
    job1 = model.Job(1, [1], date(2011, 11, 11), time(11, 30), 2)
    job2 = model.Job(1, [1], date(2011, 11, 11), time(11, 30), 2.5)
    job3 = model.Job(1, [2, 3], date(2011, 11, 11), time(11, 00), 2.5)
    assert job1.end_time == time(13, 30)
    assert job2.end_time == time(14, 00)
    assert job3.end_time == time(13, 30)


def test_employees_should_be_displayed_as_e_string():
    job1 = model.Job(1, [1], date(2011, 11, 11), time(11, 30), 2)
    job1 = model.Job(1, [1], date(2011, 11, 11), time(11, 30), 2)
    job2 = model.Job(1, [1, 4], date(2011, 11, 11), time(11, 30), 2)
    assert job1.employees == '1'
    assert job2.employees == '1,4'


def test_job_are_entities_hashed_by_customer_employee_and_date():
    job1 = model.Job(1, [1, 2, 3], date(2011, 11, 11), time(11, 30), 2)
    job2 = model.Job(1, [1, 2, 3], date(2011, 11, 11), time(11, 30), 2)
    job3 = model.Job(3, [1, 2, 3], date(2011, 11, 11), time(11, 30), 2)
    assert job1 == job2
    assert job1 != job3
    assert job2 != job3
