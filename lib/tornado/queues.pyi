import datetime
from tornado_py3.concurrent import Future
from typing import Any, Awaitable, Union

class QueueEmpty(Exception): ...
class QueueFull(Exception): ...

class _QueueIterator:
    q: Any = ...
    def __init__(self, q: Queue[_T]) -> None: ...
    def __anext__(self) -> Awaitable[_T]: ...

class Queue:
    def __init__(self, maxsize: int=...) -> None: ...
    @property
    def maxsize(self) -> int: ...
    def qsize(self) -> int: ...
    def empty(self) -> bool: ...
    def full(self) -> bool: ...
    def put(self, item: _T, timeout: Union[float, datetime.timedelta]=...) -> Future[None]: ...
    def put_nowait(self, item: _T) -> None: ...
    def get(self, timeout: Union[float, datetime.timedelta]=...) -> Awaitable[_T]: ...
    def get_nowait(self) -> _T: ...
    def task_done(self) -> None: ...
    def join(self, timeout: Union[float, datetime.timedelta]=...) -> Awaitable[None]: ...
    def __aiter__(self) -> _QueueIterator[_T]: ...

class PriorityQueue(Queue): ...
class LifoQueue(Queue): ...
