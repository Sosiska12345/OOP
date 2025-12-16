from typing import Generic, TypeVar, Optional, List

T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> Optional[T]:
        if len(self._items) == 0:
            return None
        else:
            return self._items.pop()

    def peek(self) -> Optional[T]:
        if len(self._items) == 0:
            return None
        else:
            return self._items[-1]

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
        return f"Stack({self._items})"