from datetime import date, time

from src.adapters import repository
from src.domain import model
from src.service_layer import services


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


def test_add_job():
    job = model.Job(3, [1, 5, 6], date(2021, 1, 2), time(8, 30), 1.5)
    repo = FakeRepository([])
    services.add_job(job, repo, FakeSession())
    assert repo.get(job.reference) is not None


def test_commits():
    job = model.Job(3, [1, 5, 6], date(2021, 1, 2), time(8, 30), 1.5)
    repo = FakeRepository([])
    session = FakeSession()
    services.add_job(job, repo, session)
    assert session.committed is True
