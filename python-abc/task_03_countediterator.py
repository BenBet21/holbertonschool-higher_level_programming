#!/usr/bin/python3
"""this is a CountedIterator class that extends \
the built-in iterator from the iter function"""


class CountedIterator:
    """this is a CountedIterator class that extends \
the built-in iterator from the iter function"""

    def __init__(self, item):
        self.item = item
        self.iter = iter(item)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count > len(self.item):
            raise StopIteration
        return next(self.iter)

    def get_count(self):
        return self.count
