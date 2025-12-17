from typing import TypeVar, Optional, List

T = TypeVar('T')


def create_stack() -> List[T]:
    return []


def push(stack: List[T], item: T) -> None:
    stack.append(item)


def pop(stack: List[T]) -> Optional[T]:
    if len(stack) == 0:
        return None
    else:
        return stack.pop()


def peek(stack: List[T]) -> Optional[T]:
    if len(stack) == 0:
        return None
    else:
        return stack[-1]


def size(stack: List[T]) -> int:
    return len(stack)


def is_empty(stack: List[T]) -> bool:
    return len(stack) == 0
