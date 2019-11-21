from typing import TypeVar, Generic
from decorators import class_info, member_info
from meta_info_store import MetaInfoStore

C = TypeVar("C")
M = TypeVar("M")


def nop(*_): pass


class DecorationHelper(Generic[C, M]):
    def __init__(self, name, on_complete=nop):
        self._name = name
        self._store = MetaInfoStore[C, M]()
        self._complete_callback = on_complete

    def get_store(self, cls):
        return getattr(cls, self.name, None)
    
    def class_info(self, info):
        self._store.class = info
        return class_info(self.on_complete)

    def member_info(self, info):
        return member_info(self._store, info)

    def _on_complete(self, cls):
        store = self._store
        setattr(cls, self._name, store)
        self._store = MetaInfoStore()
        self._complete_callback(cls, store)
