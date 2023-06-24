import sudoku
import random

def test_randomInt(monkeypatch):
    random.seed(123)
    monkeypatch.setattr(random, 'randint', lambda a, b: 8)

    assert sudoku.randomInt() == 8
    monkeypatch.undo()