from typing import TypeVar
from interfaces import OnDecorate
from meta_info_store import MetaInfoStore

M = TypeVar("M")


def notify_decoration(on_decorate):
    """
    Notify OnDecorate event
    :param on_decorate: OnDecorate event handler
    """
    def decorator(target):
        if callable(on_decorate):
            on_decorate(target, target.__name__)
        return target
    return decorator


def member_info(store, info):
    """
    Append member info
    :param MetaInfoStore[Any, M] store: store
    :param M info: info
    """
    def decorator(member):
        func = member.fget if isinstance(member, property) else member
        store.own_members[func.__name__] = info
        store.members[func.__name__] = info
        if isinstance(info, OnDecorate):
            info.on_decorate(member, func.__name__)
        return member
    return decorator
