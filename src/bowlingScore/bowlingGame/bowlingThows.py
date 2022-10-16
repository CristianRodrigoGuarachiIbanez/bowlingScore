from random import randint
class Throws:
    def __init__(self):
        self.pins = []
    def _saveResult(self, result):
        self.pins.append(result)
    def throw(self, start, end):
        result = randint(start, end)
        self._saveResult(result)
        return result