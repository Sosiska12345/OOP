from typing import TypeVar, Optional, Deque
from collections import deque

T = TypeVar('T')

def create_queue() -> Deque[T]:
    return deque()

def enqueue(queue: Deque[T], item: T) -> None:
    queue.append(item)

def dequeue(queue: Deque[T]) -> Optional[T]:
    if len(queue) == 0:
        return None
    else:
        return queue.popleft()

def front(queue: Deque[T]) -> Optional[T]:
    if len(queue) == 0:
        return None
    else:
        return queue[0]

def queue_size(queue: Deque[T]) -> int:
    return len(queue)

def is_queue_empty(queue: Deque[T]) -> bool:
    return len(queue) == 0

