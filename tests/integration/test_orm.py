from datetime import date, time

from src.domain import model


def test_jobs_mapper_can_load_jobs(session):
    session.execute("""
    INSERT INTO
        jobs (customer, employees, date, start_time,
        end_time, hours_number, reference)
    VALUES
        (1, '2, 3', '2021-02-01', '8:30:00', '10:30:00', 2, '12320210201');
    """)
    expected = [
        model.Job(1, [2, 3], date(2021, 2, 1), time(8, 30), 2.0)
    ]

    assert session.query(model.Job).all() == expected


def test_jobs_mapper_can_save_jobs(session):
    new_job = model.Job(1, [2, 3], date(2021, 2, 1), time(9, 0), 2)
    session.add(new_job)
    session.commit()
    expected = [
        (1, 1, '2,3', '2021-02-01', '09:00:00.000000', '11:00:00.000000', 2)
    ]

    rows = list(session.execute(
        """
        SELECT
            id, customer, employees, date, start_time, end_time, hours_number
        FROM
            jobs;
        """))

    assert rows == expected
