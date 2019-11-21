from decorators import class_info, member_info
from meta_info_store import MetaInfoStore


def nop(*_): pass


class DecorationHelper:
    def __init__(self, name, on_complete=nop):
        self._name = name
        self._store = MetaInfoStore()
        self._complete_callback = on_complete

    def get_store(self, cls):
        return getattr(cls, seelf.name, None)
    
    def class_info(self, info, on_complete):
        return class_info(store, info, self.on_complete)

    def member_info(self, info):
        return member_info(store, info)

    def _on_complete(self, cls):
        store = self._store
        setattr(cls, self._name, store)
        self._store = MetaInfoStore()
        self._complete_callback(cls, store)
