#!/us/bin/python3
""" FIFO Caching system"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO caching module"""
    def __int__(self):
        """ Init file"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Assign item key value to the dictionary"""
        if key is None or item is None:
            return
        if len(self.keys) >= self.MAX_ITEMS:
            """ """
            if key not in self.keys:
                print("DISCARD: {}".format(self.keys[0]))
                del self.cache_data[self.keys[0]]
            del self.keys[0]
        self.keys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ Return the value in self.cache_data linked to key"""
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
