from typing import Any


class Stack:
    def __init__(self):
        self._stack = []

    def put(self, elem: Any):
        self._stack.append(elem)

    def get(self) -> Any:
        return self._stack[-1]

    def delete(self):
        del self._stack[-1]

    def is_empty(self):
        return False if self._stack else True

    def get_all(self):
        return self._stack
