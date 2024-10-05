''' My Test Calculator'''
from app.main import addition

def test_addition():
    '''Addition function'''
    assert addition(1,1) == 2
