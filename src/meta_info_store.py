from typing import TypeVar, Generic, Dict

C = TypeVar("C")
M = TypeVar("M")


class MetaInfoStore(Generic[C, M]):
    def __init__(self):
        self.cls: C = None
        self.own_members: Dict[str, M] = {}
        self.members: Dict[str, M] = {}
        self.parent: MetaInfoStore or None = None

    def inherit(self, parent)
        self.parent = parent
        self.members = {**parent.members, **self.own_members}
        if isinstance(self.cls, OnInherit):
            self.cls.on_inherit(parent)

