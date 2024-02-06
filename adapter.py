from unittest import TestCase
class Square:
    def __init__(self, side=0):
        self.side = side


def calculate_area(rc):
    return rc.width * rc.height

class SquareToRectangleAdapter:
    width = 0
    height = 0
    def __init__(self, square):
        self._square = square
        self.width = square.side
        self.height = square.side


class Evaluate(TestCase):
    def test_exercise(self):
        sq = Square(11)
        adapter = SquareToRectangleAdapter(sq)
        self.assertEqual(121, calculate_area(adapter))
        sq.side = 10
        self.assertEqual(100, calculate_area(adapter))

