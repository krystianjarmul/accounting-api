from datetime import date, time

from src.adapters import repository
from src.domain import model
from src.entrypoints.app import session
from src.service_layer import services

JOBS_URL = '/jobs/'


def clear_db():
    session.query(model.Job).delete()
    session.commit()


def add_job():
    job_attrs = {
        'customer': 2,
        'employees': [2, 3],
        'date': date(2011, 1, 1),
        'start_time': time(10, 30),
        'hours_number': 2.0
    }
    repo = repository.SqlAlchemyRepository(session)
    services.create_job(**job_attrs, repo=repo, session=session)


def test_creating_a_job_successfully(client):
    payload = {
        'customer': 1,
        'employees': '1,2',
        'date': '2011-01-01',
        'start_time': '11:30:00',
        'hours_number': 2.5,
    }

    res = client.post(JOBS_URL, json=payload)
    json_data = res.get_json()

    assert res.status_code == 201
    assert json_data['customer'] == payload['customer']
    assert json_data['employees'] == payload['employees']
    assert json_data['date'] == payload['date']
    assert json_data['start_time'] == payload['start_time']
    assert json_data['hours_number'] == payload['hours_number']
    assert json_data['end_time'] == '14:00:00'


def test_creating_a_job_fails_with_invalid_payload(client):
    payload = {
        'customer': 1,
        'employees': 3,
        'date': '2011/12/3',
        'start_time': '',
        'hours_number': 2.5,
    }

    res = client.post(JOBS_URL, json=payload)

    json_data = res.get_json()

    assert res.status_code == 400


def test_retrieving_list_of_jobs(client):
    clear_db()
    add_job()

    res = client.get(JOBS_URL)

    json_data = res.get_json()

    assert res.status_code == 200
    assert json_data[0].get('id') is not None
    assert json_data[0].get('customer') is not None
    assert json_data[0].get('employees') is not None
    assert json_data[0].get('date') is not None
    assert json_data[0].get('start_time') is not None
    assert json_data[0].get('end_time') is not None
    assert json_data[0].get('hours_number') is not None
    assert json_data[0].get('reference') is not None
