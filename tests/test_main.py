''' My Test Calculator'''
import pytest
from app.main import Calculator

def test_add():
    """Test the addition operation."""
    assert Calculator.add(2, 3) == 5
    assert Calculator.history[-1] == "Added 2 + 3 = 5"

def test_subtract():
    """Test the subtraction operation."""
    assert Calculator.subtract(5, 2) == 3
    assert Calculator.history[-1] == "Subtracted 5 - 2 = 3"

def test_multiply():
    """Test the multiplication operation."""
    assert Calculator.multiply(3, 4) == 12
    assert Calculator.history[-1] == "Multiplied 3 * 4 = 12"

def test_divide():
    """Test the division operation."""
    assert Calculator.divide(10, 2) == 5.0
    assert Calculator.history[-1] == "Divided 10 / 2 = 5.0"

def test_divide_by_zero():
    """Test division by zero raises ValueError."""
    with pytest.raises(ValueError, match="Division by zero"):
        Calculator.divide(5, 0)

def test_get_last_calculation():
    """Test retrieving the last calculation from history."""
    Calculator.clear_history()
    Calculator.add(1, 1)
    assert Calculator.get_last_calculation() == "Added 1 + 1 = 2"

def test_clear_history():
    """Test clearing the calculation history."""
    Calculator.clear_history()
    Calculator.add(1, 2)
    assert len(Calculator.history) == 1
    Calculator.clear_history()
    assert len(Calculator.history) == 0
