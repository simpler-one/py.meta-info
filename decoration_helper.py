from typing import TypeVar, Generic
from decorators import class_info, member_info, OnDecorate
from meta_info_store import MetaInfoStore

C = TypeVar("C")
M = TypeVar("M")


class DecorationHelper(Generic[C, M]):
    def __init__(self, name):
        self._name = name
        self._store = MetaInfoStore[C, M]()

    def get_store(self, cls):
        return getattr(cls, self.name, None)
    
    def class_info(self, info):
        self._store.cls = info
        return class_info(self.on_complete)

    def member_info(self, info):
        return member_info(self._store, info)

    def _on_complete(self, cls):
        store = self._store
        setattr(cls, self._name, store)
        self._store = MetaInfoStore()
        if isinstance(store.cls, OnDecorate):
            store.cls.on_decorate(cls, cls.__name__)
