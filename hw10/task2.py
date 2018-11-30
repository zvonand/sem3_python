import collections
class DefCounter (collections.Counter):
    
    default_ab = -1

    def __init__(self, *args, **kwds):
        if "missing" in kwds:
            self.default_ab = kwds["missing"]
            del kwds["missing"]
        if len(args) > 1:
            raise TypeError('expected at most 1 arguments, got %d' % len(args))
        try:
            self.__root
        except AttributeError:
            self.__root = root = [None, None, None]     # sentinel node
            PREV = 0
            NEXT = 1
            root[PREV] = root[NEXT] = root
            self.__map = {}
        self.update(*args, **kwds)

    def __getitem__ (self, key):
        if key in self.keys():
            return self.get (key)
        return self.default_ab

