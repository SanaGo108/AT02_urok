import pytest
from main import count_vowels  # Замените `your_module` на имя файла с вашей функцией

def test_vowels_only():
    assert count_vowels('aeiou') == 5
    assert count_vowels('AEIOU') == 5

def test_no_vowels():
    assert count_vowels('bcdfg') == 0
    assert count_vowels('') == 0

def test_mixed_strings():
    assert count_vowels('hello') == 2
    assert count_vowels('HELLO') == 2
    assert count_vowels('Python is Fun!') == 3
    assert count_vowels('PyThOn') == 1

@pytest.mark.parametrize("test_input,expected", [
    ('aeiou', 5),
    ('AEIOU', 5),
    ('bcdfg', 0),
    ('', 0),
    ('hello', 2),
    ('HELLO', 2),
    ('Python is Fun!', 3),
    ('PyThOn', 1),
])
def test_count_vowels(test_input, expected):
    assert count_vowels(test_input) == expected