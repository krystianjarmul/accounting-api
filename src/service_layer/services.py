from typing import List
from datetime import date, time

from src.adapters.repository import AbstractRepository
from src.domain import model
from src.serializers import JobSchema
from src.service_layer import unit_of_work


def create_job(
        customer: int, employees: List[int], date: date, start_time: time,
        hours_number: float, uow: unit_of_work.AbstractUnitOfWork
) -> str:
    job = model.Job(customer, employees, date, start_time, hours_number)
    with uow:
        uow.jobs.add(job)
        uow.commit()

        job_schema = JobSchema()
        job_json = job_schema.dump(job)
    return job_json


def list_jobs(uow: unit_of_work.AbstractUnitOfWork) -> List[str]:
    with uow:
        jobs = uow.jobs.list()
        jobs_schema = JobSchema(many=True)
        jobs_jsons = jobs_schema.dump(jobs)
    return jobs_jsons
