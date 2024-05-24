#!/usr/bin/python3
"""this is a CountedIterator class that extends \
the built-in iterator from the iter function"""


class CountedIterator:
    """this is a CountedIterator class that extends \
the built-in iterator from the iter function"""

    def __init__(self, item):
        self.item = item
        self.index = 0
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= len(self.item):
            raise StopIteration 
        self.index += 1
        self.count += 1
        return self.item[self.index - 1]

    def get_count(self):
        return self.count
