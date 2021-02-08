from typing import List
from datetime import date, time

from src.adapters.repository import AbstractRepository
from src.domain import model
from src.serializers import JobSchema


def add_job(
        customer: int, employees: List[int], date: date, start_time: time,
        hours_number: float, repo: AbstractRepository, session
) -> str:
    job = model.Job(customer, employees, date, start_time, hours_number)
    repo.add(job)
    session.commit()

    job_schema = JobSchema()
    return job_schema.dump(job)


def list_jobs(repo: AbstractRepository) -> str:
    jobs = repo.list()
    jobs_schema = JobSchema(many=True)

    return jobs_schema.dump(jobs)
