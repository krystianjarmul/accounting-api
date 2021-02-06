import sys
from datetime import time, date

from flask import Flask, jsonify, request

from src.adapters.orm import start_mappers
from src.serializers import JobSchema
from src.domain import model
from src.adapters import repository
from src.database import get_session

app = Flask(__name__)

if 'pytest' in sys.modules:
    session = get_session('sqlite:///:memory:')
else:
    session = get_session('sqlite:///sqlite3.db')

start_mappers()


@app.route('/jobs/', methods=['POST'])
def add_job():
    try:
        job = model.Job(
            request.json['customer'],
            request.json['employees'],
            date.fromisoformat(request.json['date']),
            time.fromisoformat(request.json['start_time']),
            request.json['hours_number'],
        )
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

    repo = repository.SqlAlchemyRepository(session)
    repo.add(job)
    session.commit()

    job_schema = JobSchema()

    return job_schema.dump(job), 201


@app.route('/jobs/', methods=['GET'])
def list_jobs():
    session.commit()
    repo = repository.SqlAlchemyRepository(session)
    jobs = repo.list()

    jobs_schema = JobSchema(many=True)
    return jsonify(jobs_schema.dump(jobs)), 200


@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()
