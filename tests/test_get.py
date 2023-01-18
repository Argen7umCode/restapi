from requests import get
import pytest


token = 'b4522109d1a7af61e7c0d5babbe8fdb786a15ca26c2b9a8c5185f928a0c7df17'
def test_get_plate_by_id():
    id = 1
    res = get(f'http://127.0.0.1:5000/plate/get?token={token}&id={id}')
    
    assert res.json()['license_plate'] == 'К766ЕВ'
    assert res.json()['id'] == id

def test_get_plate_by_id_not_found_plate():
    id = 10000000
    res = get(f'http://127.0.0.1:5000/plate/get?token={token}&id={id}')
    
    assert res.json()['message'] == "Not found"

def test_get_plate_by_id_invalid_id():
    id = 'gfdgdfg'
    res = get(f'http://127.0.0.1:5000/plate/get?token={token}&id={id}')
    
    assert res.json()['message'] == "Invalid id"

def test_get_plate_by_id_negative_id():
    id = -1
    res = get(f'http://127.0.0.1:5000/plate/get?token={token}&id={id}')
    
    assert res.json()['message'] == "Not found"

def test_get_plate_by_id_str_id():
    id = '1'
    res = get(f'http://127.0.0.1:5000/plate/get?token={token}&id={id}')
    
    assert res.json()['license_plate'] == 'К766ЕВ'
    assert res.json()['id'] == 1

