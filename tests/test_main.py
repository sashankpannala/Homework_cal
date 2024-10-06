''' My Test Calculator'''
import pytest
from app.main import Calculator

def test_add():
    """Test addition of two numbers."""
    assert Calculator.add(1, 2) == 3
    assert Calculator.add(-1, 1) == 0
    assert Calculator.add(0, 0) == 0

def test_subtract():
    """Test subtraction of two numbers."""
    assert Calculator.subtract(5, 3) == 2
    assert Calculator.subtract(-1, -1) == 0
    assert Calculator.subtract(0, 5) == -5

def test_multiply():
    """Test multiplication of two numbers."""
    assert Calculator.multiply(3, 4) == 12
    assert Calculator.multiply(-1, 1) == -1
    assert Calculator.multiply(0, 5) == 0

def test_divide():
    """Test division of two numbers."""
    assert Calculator.divide(10, 2) == 5
    assert Calculator.divide(-6, 3) == -2
    with pytest.raises(ValueError, match="Division by zero"):
        Calculator.divide(5, 0)
