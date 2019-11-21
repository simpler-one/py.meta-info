from meta_info_store import MetaInfoStore


def class_info(store, info, on_complete):
    def decorator(cls):
        if callable(on_complete):
            on_complete(cls)
        return cls
    return decorator


def member_info(store, info):
    def decorator(member):
        func = member.fget if isinstance(member, property) else member
        store.member_info[func.__name__] = info
        return member
    return decorator


