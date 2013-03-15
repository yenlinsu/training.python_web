from persistent.mapping import PersistentMapping
from persistent import Persistent

class Deploy_Auto(PersistentMapping):
    __name__ = None
    __parent__ = None

def appmaker(zodb_root):
    if not 'app_root' in zodb_root:
        app_root = Deploy_Auto()
        zodb_root['app_root'] = app_root
        import transaction
        transaction.commit()
    return zodb_root['app_root']
