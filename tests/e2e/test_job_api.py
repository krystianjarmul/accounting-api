from src import repository

JOBS_URL = '/jobs/'


def test_creating_a_job_successfully(client):
    payload = {
        'customer': 1,
        'employees': '1, 2',
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
        'customer': 2,
        'employees': '1, 2',
        'date': '',
        'start_time': '11:30:00',
        'hours_number': 2.3,
    }

    res = client.post(JOBS_URL, json=payload)

    json_data = res.get_json()

    assert res.status_code == 400


def test_retrieving_list_of_jobs(client):
    pass
