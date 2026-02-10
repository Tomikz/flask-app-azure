import time

class SimpleCache:
    def __init__(self, ttl=60):
        self.ttl = ttl
        self.store = {}

    def get(self, key):
        value, expire = self.store.get(key, (None, 0))
        if time.time() < expire:
            return value
        else:
            self.store.pop(key, None)
            return None

    def set(self, key, value):
        self.store[key] = (value, time.time() + self.ttl)
