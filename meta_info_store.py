from typing import TypeVar, Generic, Dict

C = TypeVar("C")
P = TypeVar("P")


class MetaInfoStore(Generic[C, P]):
    def __init__(self):
        self.cls_info: C = None
        self.prop_info: Dict[str, P] = {}
