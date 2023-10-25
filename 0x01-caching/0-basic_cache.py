#!/usr/bin/python3
""" Class BasicCache that inherits from BaseCaching """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Main class BasicCache """

    def put(self, key, item):
        """ function put """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ function get """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
