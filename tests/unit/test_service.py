from datetime import date, time

from src.adapters import repository
from src.domain import model
from src.service_layer import services, unit_of_work


class FakeSession:
    committed = False

    def commit(self):
        self.committed = True


class FakeRepository(repository.AbstractRepository):

    def __init__(self, jobs):
        self._jobs = set(jobs)

    def _add(self, job):
        self._jobs.add(job)

    def _get(self, reference):
        return next(j for j in self._jobs if j.reference == reference)

    def list(self):
        return list(self._jobs)


class FakeUnitOfWork(unit_of_work.AbstractUnitOfWork):

    def __init__(self):
        self.jobs = FakeRepository([])
        self.committed = False

    def commit(self):
        self.committed = True

    def rollback(self):
        pass


def test_add_job():
    uow = FakeUnitOfWork()

    services.create_job(3, [1, 3, 6], date(2021, 1, 2), time(8, 30), 1.5, uow)

    assert uow.jobs.get('313620210102') is not None
    assert uow.committed is True


def test_list_job():
    job = model.Job(3, [1, 3, 6], date(2021, 1, 2), time(8, 30), 1.5)
    uow = FakeUnitOfWork()
    uow.jobs = FakeRepository([job])

    jobs_jsons = services.list_jobs(uow)

    assert len(jobs_jsons) == 1
    assert jobs_jsons[0].get('reference') == '313620210102'
