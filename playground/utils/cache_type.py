from enum import Enum


class RepoCacheType(Enum):
    NO_CACHE = 1
    CACHE_MISS = 2
    CACHE_HIT = 3
