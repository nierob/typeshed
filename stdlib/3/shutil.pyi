# Stubs for shutil

# Based on http://docs.python.org/3.2/library/shutil.html

# 'bytes' paths are not properly supported: they don't work with all functions,
# sometimes they only work partially (broken exception messages), and the test
# cases don't use them.

from typing import List, Iterable, Callable, Any, Tuple, Sequence, IO, AnyStr

def copyfileobj(fsrc: IO[AnyStr], fdst: IO[AnyStr],
                length: int = ...) -> None: ...

def copyfile(src: str, dst: str) -> None: ...
def copymode(src: str, dst: str) -> None: ...
def copystat(src: str, dst: str) -> None: ...
def copy(src: str, dst: str) -> None: ...
def copy2(src: str, dst: str) -> None: ...
def ignore_patterns(*patterns: str) -> Callable[[str, List[str]],
                                                Iterable[str]]: ...
def copytree(src: str, dst: str, symlinks: bool = ...,
             ignore: Callable[[str, List[str]], Iterable[str]] = ...,
             copy_function: Callable[[str, str], None] = ...,
             ignore_dangling_symlinks: bool = ...) -> None: ...
def rmtree(path: str, ignore_errors: bool = ...,
           onerror: Callable[[Any, str, Any], None] = ...) -> None: ...
def move(src: str, dst: str) -> None: ...

class Error(Exception): ...

def make_archive(base_name: str, format: str, root_dir: str = ...,
                 base_dir: str = ..., verbose: bool = ...,
                 dry_run: bool = ..., owner: str = ..., group: str = ...,
                 logger: Any = ...) -> str: ...
def get_archive_formats() -> List[Tuple[str, str]]: ...
def register_archive_format(name: str, function: Any,
                            extra_args: Sequence[Tuple[str, Any]] = ...,
                            description: str = ...) -> None: ...
def unregister_archive_format(name: str) -> None: ...
def unpack_archive(filename: str, extract_dir: str = ...,
                   format: str = ...) -> None: ...
def register_unpack_format(name: str, extensions: List[str], function: Any,
                           extra_args: Sequence[Tuple[str, Any]] = ...,
                           description: str = ...) -> None: ...
def unregister_unpack_format(name: str) -> None: ...
def get_unpack_formats() -> List[Tuple[str, List[str], str]]: ...

# Introduced in python 3.3
import os
def which(cmd: str, mode: Any=os.F_OK | os.X_OK, path: Any=None) -> str: ...