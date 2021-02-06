from datetime import date, time

from src.domain import model
from src.adapters import repository


def test_repository_can_save_jobs(session):
    job = model.Job(1, [1, 3], date(2021, 1, 2), time(11, 30), 2)

    repo = repository.SqlAlchemyRepository(session)
    repo.add(job)
    session.commit()

    rows = list(session.execute(
        'SELECT date, start_time, end_time, employees FROM jobs'
    ))

    assert rows == [('2021-01-02', '11:30:00.000000', '13:30:00.000000', '1,3')]


def test_repository_can_retrieve_list_of_jobs(session):
    session.execute("""
    INSERT INTO jobs
    (customer, employees, date, start_time, end_time, hours_number, reference)
    VALUES
        (1, '2,4', '2021-10-11', '11:30:00', '13:30:00', 2, '12420211011'),
        (2, '1,5', '2021-09-12', '15:00:00', '16:00:00', 1, '21520210912')
    """)
    session.commit()

    repo = repository.SqlAlchemyRepository(session)
    jobs = repo.list()

    assert jobs == [
        model.Job(1, [2, 4], date(2021, 10, 11), time(13, 30), 2),
        model.Job(2, [1, 5], date(2021, 9, 12), time(15, 00), 1)
    ]
