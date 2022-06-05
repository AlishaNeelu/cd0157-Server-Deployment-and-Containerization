'''
Tests for jwt flask app.
'''
import os
import json
import pytest

import main

SECRET = 'myjwtsecret' 
TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NTU2MzY5ODksIm5iZiI6MTY1NDQyNzM4OSwiZW1haWwiOiJzeWVka2hhbGVlcUBnbWFpbC5jb20ifQ.loGSpCvPj9nV0fpPKMkdMd09vJn21ZzQKNY4LzEeAZY'
EMAIL = 'syedkhaleeq@gmail.com'
PASSWORD = 'India@123'

@pytest.fixture
def client():
    os.environ['JWT_SECRET'] = SECRET
    main.APP.config['TESTING'] = True
    client = main.APP.test_client()

    yield client



def test_health(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == 'Healthy'


def test_auth(client):
    body = {'email': EMAIL,
            'password': PASSWORD}
    response = client.post('/auth', 
                           data=json.dumps(body),
                           content_type='application/json')

    assert response.status_code == 200
    token = response.json['token']
    assert token is not None
