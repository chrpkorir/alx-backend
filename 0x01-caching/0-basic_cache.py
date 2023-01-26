#!/usr/bin/python3
""" Caching system """
BasicCaching = __import__('base_cache').BaseCaching

class BasicCache(BasicCaching):
    """ caching system"""

    def put(self, key, item):
        """ Assigns the dictionary self.cache_data
        the key if none do nothing """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Return value linked to key in self.
        cache_data """
        if not key or key not in self.cache_data.keys():
            return self.cache_data[key]
