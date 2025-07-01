from .array import Array
from typing import NamedTuple, Any



# The Pair class consists of the .key and .value attributes,
# which are free to take values of any data type.

class Pair(NamedTuple):
    key : Any
    value : Any


DELETED = object()



class HashTable:
    def __init__(self, capacity=8, load_factor_threshold=0.7):
        if capacity < 1:
            raise ValueError("Capacity must be be a positive number")
        if not (0 < load_factor_threshold <= 1):
            raise ValueError("Load factor must be a number between(0, 1]")
        self._pairs = capacity * [None]
        self._load_factor_threshold = load_factor_threshold



    def __len__(self):
        return len(self._pairs)
    

    
    def __setitem__(self, key, value):
        if self.load_factor >= self._load_factor_threshold:
            self._resize_and_rehash()
        for index, pair in self._prob(key):
            if pair is DELETED: continue
            if pair is None or pair.key == key:
                self._pairs[index] = Pair(key, value)
                break
        else:
            self._resize_and_rehash()
            self[key] = value



    def _resize_and_rehash(self):
        copy = HashTable(capacity=self.capacity * 2)
        for key, value in self.pairs:
            copy[key] = value
            self._pairs = copy._pairs



    def __getitem__(self, key):
        for _, pair in self._prob(key):
            if pair is None:
                return False
            if pair is DELETED:
                continue
            if pair.key == key:
                return pair.value
        raise KeyError(key)
    


    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True



    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default



    def __delitem__(self, key):
        for index, pair in self._prob(key):
            if pair is None:
                raise KeyError(key)
            if pair is DELETED:
                continue
            if pair.key == key:
                self._pairs[index] = DELETED
                break
        else:
            raise KeyError(key)




    def __iter__(self):
        yield from self.keys
    


    def __str__(self): 
        pairs = Array()
        for key, value in self.pairs:
            pairs.append(f"{key!r}: {value!r}")
        return "{" + ", ".join(pairs) + "}"
    


    def _prob(self, key):
        index = self._index(key)
        for _ in range(self.capacity):
            yield index, self._pairs[index]
            index = (index + 1) % self.capacity


    # When you request a list of key-value pairs stored in your hash table,
    # you’ll get their shallow copy each time
    @property
    def pairs(self):
        pairs = Array()
        for pair in self._pairs:
            if pair is not None and pair is not DELETED:   # to filter empty values out
                pairs.append(pair)
        return pairs
    


    @property
    def values(self):
        values = Array()
        for pair in self.pairs:
            values.append(pair.value)
        return values
    


    @property
    def keys(self):
        keys = Array()
        for pair in self.pairs:
            keys.append(pair.key)
        return keys



    @property
    def capacity(self):
        return len(self._pairs)


    @property
    def load_factor(self):
        occupied_or_deleted = 0
        for slot in self._pairs:
            if slot:
                occupied_or_deleted += 1
                
        return occupied_or_deleted / self.capacity



    def _index(self, key):
        return self.hash_function(key) % self.capacity



    def hash_function(self, key):
        return sum(
            index * ord(character)
            for index, character in enumerate(repr(key).lstrip("'"), 1)
        )
