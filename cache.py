import time
from typing import Any, Optional
import json

class SimpleCache:
    def __init__(self, default_ttl: int = 300):  # 5min default
        self.cache = {}
        self.ttls = {}
        self.default_ttl = default_ttl
    
    def get(self, key: str) -> Optional[Any]:
        if key in self.cache:
            if time.time() < self.ttls.get(key, 0):
                return self.cache[key]
            else:
                # Expired
                del self.cache[key]
                del self.ttls[key]
        return None
    
    def set(self, key: str, value: Any, ttl: Optional[int] = None):
        ttl_seconds = ttl or self.default_ttl
        self.cache[key] = value
        self.ttls[key] = time.time() + ttl_seconds
    
    def clear(self, key: str):
        if key in self.cache:
            del self.cache[key]
            del self.ttls[key]

#global cache instance
cache = SimpleCache()