# Bao Dinh
# LEAP Life Day 1
# PyTest example
# pip install -U pytest

def func(x) -> int: 
    return x + 1

def test_answer() -> None: 
    assert func(4) == 5
    # assert func(3) == 5 # Causes pytest to fail and spams actions notifications
