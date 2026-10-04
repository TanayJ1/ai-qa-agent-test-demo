from app.calculator import add, subtract


def test_addition_passes():
    assert add(2, 3) == 5


def test_subtraction_intentional_failure():
    # Intentional incorrect expectation for the QA demo.
    assert subtract(7, 3) == 3
