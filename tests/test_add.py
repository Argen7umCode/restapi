from requests import post
import pytest


token = 'b4522109d1a7af61e7c0d5babbe8fdb786a15ca26c2b9a8c5185f928a0c7df17'
def test_add_plate_already_exist():
    data = {
        'token' : token,
        'plate' : 'В609АХ'
    }

    res = post(f'http://127.0.0.1:5000/plate/add', json=data)
    print(res.json())
    assert res.json()['message'] == 'Already exist'


def test_add_plate_invalid_plate():
    data = {
        'token' : token,
        'plate' : 'fsda'
    }

    res = post(f'http://127.0.0.1:5000/plate/add', json=data)
    print(res.json())
    assert res.json()['message'] == 'Invalid plate'



