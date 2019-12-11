from typing import TypeVar, Generic, Dict
from interferences import OnInherit

C = TypeVar("C")
M = TypeVar("M")


class MetaInfoStore(Generic[C, M]):
    def __init__(self):
        self.cls: C = None
        self.own_members: Dict[str, M] = {}
        self.members: Dict[str, M] = {}

    def inherit(self, parent):
        """
        Inherit
        :param MetaInfoStore parent:
        """
        self.members = {**parent.members, **self.own_members}
        if isinstance(self.cls, OnInherit):
            self.cls.on_inherit(parent.cls)
