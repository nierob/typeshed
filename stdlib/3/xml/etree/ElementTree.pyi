# Stubs for xml.etree.ElementTree (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
import io

VERSION = ... # type: Any

class ParseError(SyntaxError): ...

def iselement(element): ...

class Element:
    def __init__(self, tag, attrib=..., **extra) -> None: ...
    def append(self, *args, **kwargs): ...
    def clear(self, *args, **kwargs): ...
    def extend(self, *args, **kwargs): ...
    def find(self, *args, **kwargs): ...
    def findall(self, *args, **kwargs): ...
    def findtext(self, match, default=..., namespaces=...): ...
    def get(self, *args, **kwargs): ...
    def getchildren(self): ...
    def getiterator(self, tag=...): ...
    def insert(self, *args, **kwargs): ...
    def items(self, *args, **kwargs): ...
    def iter(self, *args, **kwargs): ...
    def iterfind(self, match, namespaces=...): ...
    def itertext(self): ...
    def keys(self): ...
    def makeelement(self, tag, attrib): ...
    def remove(self, *args, **kwargs): ...
    def set(self, *args, **kwargs): ...
    def __copy__(self): ...
    def __deepcopy__(self): ...
    def __delattr__(self, name): ...
    def __delitem__(self, name): ...
    def __getitem__(self, name): ...
    def __getstate__(self): ...
    def __len__(self): ...
    def __setattr__(self, name, value): ...
    def __setitem__(self, index, object): ...
    def __setstate__(self, state): ...
    def __sizeof__(self): ...

def SubElement(parent, tag, attrib=..., **extra): ...
def Comment(text=...): ...
def ProcessingInstruction(target, text=...): ...

PI = ... # type: Any

class QName:
    text = ... # type: Any
    def __init__(self, text_or_uri, tag=...) -> None: ...
    def __hash__(self): ...
    def __le__(self, other): ...
    def __lt__(self, other): ...
    def __ge__(self, other): ...
    def __gt__(self, other): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

class ElementTree:
    def __init__(self, element=..., file=...) -> None: ...
    def getroot(self): ...
    def parse(self, source, parser=...): ...
    def iter(self, tag=...): ...
    def getiterator(self, tag=...): ...
    def find(self, path, namespaces=...): ...
    def findtext(self, path, default=..., namespaces=...): ...
    def findall(self, path, namespaces=...): ...
    def iterfind(self, path, namespaces=...): ...
    def write(self, file_or_filename, encoding=..., xml_declaration=..., default_namespace=..., method=..., *, short_empty_elements=...): ...
    def write_c14n(self, file): ...

def register_namespace(prefix, uri): ...
def tostring(element, encoding=..., method=..., *, short_empty_elements=...): ...

class _ListDataStream(io.BufferedIOBase):
    lst = ... # type: Any
    def __init__(self, lst) -> None: ...
    def writable(self): ...
    def seekable(self): ...
    def write(self, b): ...
    def tell(self): ...

def tostringlist(element, encoding=..., method=..., *, short_empty_elements=...): ...
def dump(elem): ...
def parse(source, parser=...): ...
def iterparse(source, events=..., parser=...): ...

class XMLPullParser:
    def __init__(self, events=..., *, _parser=...) -> None: ...
    def feed(self, data): ...
    def close(self): ...
    def read_events(self): ...

class _IterParseIterator:
    root = ... # type: Any
    def __init__(self, source, events, parser, close_source=...) -> None: ...
    def __next__(self): ...
    def __iter__(self): ...

def XML(text, parser=...): ...
def XMLID(text, parser=...): ...

fromstring = ... # type: Any

def fromstringlist(sequence, parser=...): ...

class TreeBuilder:
    def __init__(self, element_factory=...) -> None: ...
    def close(self): ...
    def data(self, data): ...
    def start(self, tag, attrs): ...
    def end(self, tag): ...

class XMLParser:
    target = ... # type: Any
    entity = ... # type: Any
    version = ... # type: Any
    def __init__(self, html=..., target=..., encoding=...) -> None: ...
    def _parse_whole(self, *args, **kwargs): ...
    def _setevents(self, *args, **kwargs): ...
    def close(self, *args, **kwargs): ...
    def doctype(self, name, pubid, system): ...
    def feed(self, data): ...
