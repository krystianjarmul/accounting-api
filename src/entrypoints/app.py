import sys
from datetime import time, date

from flask import Flask, jsonify, request

from src.adapters.orm import start_mappers

from src.domain import model
from src.adapters import repository
from src.database import get_session
from src.service_layer import services, unit_of_work

app = Flask(__name__)

if 'pytest' in sys.modules:
    session = get_session('sqlite:///:memory:')
else:
    session = get_session('sqlite:///sqlite3.db')

start_mappers()


@app.route('/jobs/', methods=['POST'])
def create_job():
    try:
        correct_date = date.fromisoformat(request.json['date'])
        correct_time = time.fromisoformat(request.json['start_time'])
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

    uow = unit_of_work.SqlAlchemyUnitOfWork(session)
    job_json = services.create_job(
        request.json['customer'],
        request.json['employees'],
        correct_date,
        correct_time,
        request.json['hours_number'],
        uow
    )

    return job_json, 201


@app.route('/jobs/', methods=['GET'])
def list_jobs():
    uow = unit_of_work.SqlAlchemyUnitOfWork(session)
    with uow:
        jobs_jsons = services.list_jobs(uow)

    return jsonify(jobs_jsons), 200


@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()
