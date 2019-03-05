from cacheout import Cache


cache = Cache()
def setCache(key, value):
    cache.set(key, value)

def getCache(key):
    return cache.get(key)

def deleteCash(key):
    cache.delete(key)