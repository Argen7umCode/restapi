import pytest
from requests import get


token = 'b4522109d1a7af61e7c0d5babbe8fdb786a15ca26c2b9a8c5185f928a0c7df17'
def test_get_gen_plates():
    amount = 2
    res = get(f'http://127.0.0.1:5000/plate/generate?token={token}&amount={amount}')
    
    assert len(res.json()) == amount


def test_get_gen_plates_negtive_amount():
    amount = -1
    res = get(f'http://127.0.0.1:5000/plate/generate?token={token}&amount={amount}')

    assert res.json()['message'] == 'Invalid amount'


def test_get_gen_plates_str_amount():
    amount = 'fdsd'
    res = get(f'http://127.0.0.1:5000/plate/generate?token={token}&amount={amount}')

    assert res.json()['message'] == 'Invalid amount'


def test_get_gen_plates_dif_amount():
    amount = 2000
    res = get(f'http://127.0.0.1:5000/plate/generate?token={token}&amount={amount}')
    
    assert len(res.json()) == amount
