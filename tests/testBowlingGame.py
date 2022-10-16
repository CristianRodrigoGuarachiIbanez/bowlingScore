import unittest
from bowlingScore.bowlingGame import BowlingGame, Throws


class TestBowlingScore(unittest.TestCase):
    def reset(self):
        self.game = BowlingGame()
        self.throws = Throws()

    def testAllOnes(self):
        self.rollMany(0, 1, 20)
        assert self.game.score() == 20

    def testOneSpare(self):
        self.game.roll(5, 0)
        self.game.roll(5, 1)
        self.game.roll(3, 2)
        self.rollMany(3, 0, 17)
        assert self.game.score() == 16

    def testOneStrike(self):
        self.game.roll(10, 0)
        self.game.roll(5, 1)
        self.game.roll(3, 2)
        self.rollMany(3, 0, 17)
        assert self.game.score() == 26

    def testPerfectGame(self):
        self.rollMany(0, 10, 12)
        assert self.game.score() == 300

    def testAllSpares(self):
        self.rollMany(0, 5, 21)
        assert self.game.score() == 150

    def testThrows(self):
        for i in range(20):
            self.game.roll(self.throws.throw(1,11), i)

    def rollMany(self, start, pins, rolls):
        for i in range(start, rolls):
            self.game.roll(pins, i)

if __name__ == "__main__":
    pass