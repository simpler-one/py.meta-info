from meta_info_store import MetaInfoStore


def notify_decoration(on_decorate):
    def decorator(target):
        if callable(on_decorate):
            on_decorate(target)
        return target
    return decorator


def member_info(store, info):
    def decorator(member):
        func = member.fget if isinstance(member, property) else member
        store.members[func.__name__] = info
        return member
    return decorator


