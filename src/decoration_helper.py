from typing import TypeVar, Generic
from interfaces import OnDecorate
from .decorators import notify_decoration, member_info
from .meta_info_store import MetaInfoStore

C = TypeVar("C")
M = TypeVar("M")


class DecorationHelper(Generic[C, M]):
    def __init__(self, name, *, inherit=True):
        self._name = name
        self._inherit = inherit
        self._store = MetaInfoStore[C, M]()

    def get_store(self, cls):
        return getattr(cls, self._name, None)
    
    def class_info(self, info):
        self._store.cls = info
        return notify_decoration(self._on_complete)

    def member_info(self, info):
        return member_info(self._store, info)

    def _on_complete(self, cls, cls_name):
        store = self._store
        parent = getattr(cls, self._name, None)
        setattr(cls, self._name, store)
        self._store = MetaInfoStore()

        if isinstance(store.cls, OnDecorate):
            store.cls.on_decorate(cls, cls_name)

        if self._inherit and parent is not None:
            store.inherit(parent)
