from meta_info_store import MetaInfoStore

_TEMPORARY_STORE = {}
""" :type: typing.Dict[str, MetaInfoStore] """


def class_info(store, info):
    def decorator(cls):
        
        return cls
    return decorator


def member_info(store, info):
    st = _get_store(store)
    def decorator(member):
        st.member_info[member.__name__] = info
        return member
    return decorator


def _get_store(store):
    if isinstance(store, str):
        st = _TEMPORARY_STORE.get(store)
        if st is None:
            st = MetaInfoStore()
            _TEMPORARY_STORE[store] = st
        return st
    elif isinstance(store, MetaInfoStore):
        return store
    else:
        raise TypeError(f"store must be str or MetaInfoStore but got: {type(store)}")
