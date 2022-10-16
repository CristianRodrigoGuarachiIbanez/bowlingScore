
class BowlingGame:
    def __init__(self):
        self._rolls = [0 for _ in range(20)]

    def roll(self, pins: int, index: int):
        self._rolls[index] = pins

    def getRolls(self):
        return self._rolls

    def score(self):
        result = 0
        rollIndex = 0
        FRAMES = 10
        for frameIndex in range(FRAMES):
            if(self._isStrike(rollIndex)):
                result += self._strikeScore(rollIndex)
                rollIndex += 1
            elif(self._isSpare(rollIndex)):
                result+= self._spareScore(rollIndex)
                rollIndex += 2
            else:
                result += self._frameScore(rollIndex)
                rollIndex +=2
        return result

    def _isStrike(self, rollIndex: int) -> bool:
        return self._rolls[rollIndex] == 10

    def _isSpare(self, rollIndex: int) -> bool:
        try:
            return self._rolls[rollIndex] + self._rolls[rollIndex + 1] ==10
        except IndexError:
            return False

    def _spareScore(self, rollIndex: int) -> int:
        try:
            return 10 + self._rolls[rollIndex + 2]
        except IndexError:
            return 10 + 0

    def _strikeScore(self, rollIndex: int) -> int:
        try:
            return 10 + self._rolls[rollIndex + 1] + self._rolls[rollIndex + 2]
        except IndexError:
            return self._rolls[rollIndex] + 0

    def _frameScore(self, rollIndex: int) -> int:
        try:
            return self._rolls[rollIndex] + self._rolls[rollIndex + 1]
        except IndexError:
            return self._rolls[rollIndex] + 0


if __name__ == "__main__":

    pass