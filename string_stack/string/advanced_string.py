from string_stack.string import String
from typing import List


class AdvancedString(String):
    def __init__(self, chars):
        super().__init__(chars)

    def get_chars(self, offset: (int, None) = None, limit: (int, None) = None) -> List[str]:
        return self._chars[offset:limit]
