from queue import PriorityQueue


# todo test
class Item:
    def __init__(self, key: float, value) -> None:
        self._key = key
        self._value = value

    def __ge__(self, other) -> bool:
        return self.key >= other.key

    def __gt__(self, other) -> bool:
        return self.key > other.key

    def __eq__(self, other) -> bool:
        return self.key == other.key

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __le__(self, other) -> bool:
        return self.key <= other.key

    def __lt__(self, other) -> bool:
        return self.key < other.key

    @property
    def key(self) -> float:
        return self._key

    @property
    def value(self):
        return self._value


# todo test
class Holder:
    _MIN_SIZE = 1
    _MAX_SIZE = 100
    _DEFAULT_SIZE = 10

    def __init__(self, size=None) -> None:
        self._max_size = 1 + size \
            if isinstance(size, int) and self._MIN_SIZE <= size <= self._MAX_SIZE \
            else self._DEFAULT_SIZE
        self._queue = PriorityQueue(self._max_size)

    def add(self, key: float, value) -> None:
        item = Item(key, value)
        if self._max_size - 1 > self._queue.qsize():
            self._queue.put(item)
        else:
            self._queue.put(item)
            self._queue.get()

    def get(self) -> tuple:
        result = []
        for _ in range(self._queue.qsize()):
            result.append(self._queue.get().value)
        return tuple(result)
