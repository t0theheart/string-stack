

class String:
    def __init__(self, chars: str = ''):
        assert isinstance(chars, str), 'String constructor takes only literal'
        self._chars = [char for char in chars if chars]
        self._length = len(self._chars)

    @property
    def length(self) -> int:
        return self._length

    def clear(self):
        self._chars = []
        self._length = 0
