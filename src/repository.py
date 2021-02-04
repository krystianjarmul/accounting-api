import abc
from typing import List

from . import model


class AbstractRepository(abc.ABC):

    def get(self, job_id: str) -> model.Job:
        return self._get(job_id)

    def add(self, job: model.Job):
        self._add(job)

    @abc.abstractmethod
    def _get(self, job_id: str):
        raise NotImplementedError

    @abc.abstractmethod
    def _add(self, job):
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):

    def __init__(self, session):
        self.session = session

    def _get(self, job_id):
        return self.session.query(model.Job).filter_by(job_id=job_id).one()

    def _add(self, job):
        self.session.add(job)

    def list(self) -> List[model.Job]:
        return self.session.query(model.Job).all()
