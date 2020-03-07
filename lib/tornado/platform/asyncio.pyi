import asyncio
import concurrent.futures
from tornado_py3.gen import convert_yielded as convert_yielded
from tornado_py3.ioloop import IOLoop as IOLoop, _Selectable
from typing import Any, Awaitable, Callable, Optional, Union

class BaseAsyncIOLoop(IOLoop):
    asyncio_loop: Any = ...
    handlers: Any = ...
    readers: Any = ...
    writers: Any = ...
    closing: bool = ...
    def initialize(self, asyncio_loop: asyncio.AbstractEventLoop, **kwargs: Any) -> None: ...
    def close(self, all_fds: bool=...) -> None: ...
    def add_handler(self, fd: Union[int, _Selectable], handler: Callable[..., None], events: int) -> None: ...
    def update_handler(self, fd: Union[int, _Selectable], events: int) -> None: ...
    def remove_handler(self, fd: Union[int, _Selectable]) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def call_at(self, when: float, callback: Callable[..., None], *args: Any, **kwargs: Any) -> object: ...
    def remove_timeout(self, timeout: object) -> None: ...
    def add_callback(self, callback: Callable, *args: Any, **kwargs: Any) -> None: ...
    def add_callback_from_signal(self, callback: Callable, *args: Any, **kwargs: Any) -> None: ...
    def run_in_executor(self, executor: Optional[concurrent.futures.Executor], func: Callable[..., _T], *args: Any) -> Awaitable[_T]: ...
    def set_default_executor(self, executor: concurrent.futures.Executor) -> None: ...

class AsyncIOMainLoop(BaseAsyncIOLoop):
    def initialize(self, **kwargs: Any) -> None: ...
    def make_current(self) -> None: ...

class AsyncIOLoop(BaseAsyncIOLoop):
    is_current: bool = ...
    def initialize(self, **kwargs: Any) -> None: ...
    def close(self, all_fds: bool=...) -> None: ...
    old_asyncio: Any = ...
    def make_current(self) -> None: ...

def to_tornado_future(asyncio_future: asyncio.Future) -> asyncio.Future: ...
def to_asyncio_future(tornado_future: asyncio.Future) -> asyncio.Future: ...

class AnyThreadEventLoopPolicy(_BasePolicy):
    def get_event_loop(self) -> asyncio.AbstractEventLoop: ...
