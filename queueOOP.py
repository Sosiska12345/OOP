from typing import Generic, TypeVar, Optional, Deque
from collections import deque

T = TypeVar('T')


class Queue(Generic[T]):
    def __init__(self) -> None:
        self._items: Deque[T] = deque()

    def enqueue(self, item: T) -> None:
        self._items.append(item)

    def dequeue(self) -> Optional[T]:
        if len(self._items) == 0:
            return None
        else:
            return self._items.popleft()

    def front(self) -> Optional[T]:
        if len(self._items) == 0:
            return None
        else:
            return self._items[0]

    def size(self) -> int:
        return len(self._items)

    def is_empty(self) -> bool:
        if len(self._items) == 0:
            return True
        else:
            return False

    def __len__(self) -> int:
        return len(self._items)

    def __str__(self) -> str:
        return f"Queue({list(self._items)})"