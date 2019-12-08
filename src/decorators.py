from abc import ABC, abstractmethod
from meta_info_store import MetaInfoStore


def notify_decoration(on_decorate):
    def decorator(target):
        if callable(on_decorate):
            on_decorate(target, target.__name__)
        return target
    return decorator


def member_info(store, info):
    def decorator(member):
        func = member.fget if isinstance(member, property) else member
        store.members[func.__name__] = info
        if isinstance(info, OnDecorate):
            info.on_decorate(member, func.__name__)
        return member
    return decorator


class OnDecorate(ABC):
    @abstractmethod
    def on_decorate(self, target, name):
        raise NotImplementedError()
