from datetime import date, time

from src.adapters import repository
from src.service_layer import unit_of_work
from src.domain import model


def add_job(session):
    job_attrs = {
        'customer': 2,
        'employees': [2, 3],
        'date': date(2011, 1, 1),
        'start_time': time(10, 30),
        'hours_number': 2.0
    }
    repo = repository.SqlAlchemyRepository(session)
    repo.add(model.Job(*job_attrs.values()))
    session.commit()


def get_created_job(session):
    [[reference]] = session.execute(
        """SELECT reference FROM jobs WHERE customer=1 AND
                                            date='2021-01-02' AND
                                            start_time='11:30:00.000000'
        """
    )
    return reference


def test_uow_can_add_a_job(session):
    job = model.Job(1, [2, 3], date(2021, 1, 2), time(11, 30), 2.5)
    uow = unit_of_work.SqlAlchemyUnitOfWork(session)
    with uow:
        uow.jobs.add(job)
        uow.commit()

    assert get_created_job(session) == '12320210102'


def test_uow_can_retrieve_list_of_jobs(session):
    add_job(session)

    uow = unit_of_work.SqlAlchemyUnitOfWork(session)
    with uow:
        jobs = uow.jobs.list()

        jobs_count = len(jobs)
        reference = jobs[0].reference
    assert jobs_count == 1
    assert reference == '22320110101'
