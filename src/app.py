import os
from datetime import time, date

from flask import Flask, jsonify, request
from sqlalchemy.orm import sessionmaker

from .config import get_production_engine, get_test_engine
from .orm import metadata, start_mappers
from .serializers import JobSchema
from sqlalchemy import create_engine

from . import model
from . import repository

TEST_ENV = int(os.environ.get('TEST', 1))
if TEST_ENV:
    engine = get_test_engine()
else:
    engine = get_production_engine()

start_mappers()
session = sessionmaker(bind=engine)()
metadata.create_all(engine)

app = Flask(__name__)


@app.route('/jobs/create', methods=['POST'])
def add_job():
    try:
        job = model.Job(
            request.json['customer'],
            request.json['employees'],
            date.fromisoformat(request.json['date']),
            time.fromisoformat(request.json['start_time']),
            request.json['hours_number'],
        )
        repo = repository.SqlAlchemyRepository(session)
        repo.add(job)
        session.commit()

        job_schema = JobSchema()

        return job_schema.dump(job), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/jobs/', methods=['GET'])
def list_jobs():
    session.commit()
    repo = repository.SqlAlchemyRepository(session)
    jobs = repo.list()

    jobs_schema = JobSchema(many=True)
    return jsonify(jobs_schema.dump(jobs)), 200
