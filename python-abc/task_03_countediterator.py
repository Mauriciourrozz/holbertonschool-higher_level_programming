#!/usr/bin/python3
class CountedIterator:
    def __init__(self, i):
        self.i = iter(i)
        self.count = 0
    
    def get_count(self):
        return self.count
    
    def __next__(self):
        x = next(self.i)
        self.count += 1
        return x
