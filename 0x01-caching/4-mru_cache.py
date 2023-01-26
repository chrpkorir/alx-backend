#!/usr/bin/python3
""" """
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ """
    def __int__(self):
        """ """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ """
        if key is None or item is None:
            return
        if len(self.keys) >= self.MAX_ITEMS:
            if key not in self.keys:
                print("DISCARD: {}".format(self.keys[0]))
                del self.cache_data[self.keys[0]]
            del self.keys[0]
        self.keys = [key] + self.keys
        self.cache_data[key] = item

    def get(self, key):
        """ """
        if not key or key not in self.cache_data.keys():
            return None
        del self.keys[self.keys.index(key)]
        self.keys = [key] + self.keys
        return self.cache_data[key]