from typing import TypeVar, Generic, Dict

C = TypeVar("C")
M = TypeVar("M")


class MetaInfoStore(Generic[C, M]):
    def __init__(self):
        self.class: C = None
        self.members: Dict[str, M] = {}
