from decorators import class_info, member_info
from meta_info_store import MetaInfoStore


class DecorationHelper:
    def __init__(self, name):
        self._name = name
        self._store = MetaInfo

    def get_store(self, cls):
        return getattr(cls, seelf.name, None)
    
    def class_info(self, info):
        return class_info(store, info, True)

    def member_info(self, info):
        return member_info(store, info)
