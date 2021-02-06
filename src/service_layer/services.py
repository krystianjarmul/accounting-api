from src.adapters.repository import AbstractRepository
from src.domain.model import Job


def add_job(job: Job, repo: AbstractRepository, session) -> str:
    repo.add(job)
    session.commit()
