import math_func
import pytest

@pytest.mark.p1
def test_add():
    assert math_func.add(7,3) == 10
    assert math_func.add(7) == 9
    assert math_func.add(5) == 7

@pytest.mark.p1
def test_product():
    assert math_func.product(5, 2) == 10
    assert math_func.product(5) == 10

@pytest.mark.p2
def test_add_strings():
    result = math_func.add('hello ','world')
    assert result =='hello world'
    assert type(result) is str
    assert 'heldlo' not in result

@pytest.mark.p2
def test_product_strings():
    assert math_func.product('hello ',3) == 'hello hello hello '
    result = math_func.product('hello ')
    assert result == 'hello hello '
    assert type(result) is str
    assert 'hello' in result