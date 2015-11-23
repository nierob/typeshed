"""The asyncio package, tracking PEP 3156."""
from asyncio.futures import (
    Future as Future,
)
from asyncio.tasks import (
    coroutine as coroutine,
    sleep as sleep,
    Task as Task,
    FIRST_COMPLETED as FIRST_COMPLETED,
    FIRST_EXCEPTION as FIRST_EXCEPTION,
    ALL_COMPLETED as ALL_COMPLETED,
    wait as wait,
    wait_for as wait_for,
)
from asyncio.events import (
    AbstractEventLoopPolicy as AbstractEventLoopPolicy,
    AbstractEventLoop as AbstractEventLoop,
    Handle as Handle,
    get_event_loop as get_event_loop, 
    Event
)
from asyncio.queues import (
    Queue as Queue,
    PriorityQueue as PriorityQueue,
    LifoQueue as LifoQueue,
    JoinableQueue as JoinableQueue,
    QueueFull as QueueFull,
    QueueEmpty as QueueEmpty,
)

class CancelledError(Exception):
    def __init__(self, *args, **keys) -> None: pass
    
class TimeoutError(Exception):
    def __init__(self, *args, **keys) -> None: pass
    

# Deprecated since version 3.4.4.
def async(coro_or_future, *, loop: AbstractEventLoop=None) -> Future: pass

def gather(*coros_or_futures, loop: AbstractEventLoop=None, return_exceptions: bool=False) -> Future: pass
def shield(arg, *, loop: AbstractEventLoop=None): pass

__all__ = (futures.__all__ +
            tasks.__all__ +
            events.__all__ +
            queues.__all__
            + ['TimeoutError', 'CancelledError', 'gather', 'async', 'shield'])
