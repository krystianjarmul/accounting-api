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
    repo, session = FakeRepository([]), FakeSession()

    services.create_job(
        3, [1, 3, 6], date(2021, 1, 2), time(8, 30), 1.5, repo, session
    )

    assert repo.get('313620210102') is not None
    assert session.committed is True


def test_list_job():
    job = model.Job(3, [1, 3, 6], date(2021, 1, 2), time(8, 30), 1.5)
    repo, session = FakeRepository([job]), FakeSession()

    jobs_jsons = services.list_jobs(repo)

    assert len(jobs_jsons) == 1
    assert jobs_jsons[0].get('customer') is not None
    assert jobs_jsons[0].get('date') is not None
    assert jobs_jsons[0].get('end_time') is not None
    assert jobs_jsons[0].get('reference') is not None
