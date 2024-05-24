#!/usr/bin/python3
"""this is an VerboseList classe that inherits from the built-in list class"""


class VerboseList(list):
    """this Verboselist class inherits from list"""

    def append(self, item):
        super().append(item)
        print("Added [{}] to the list".format(item))

    def extend(self, item):
        super().extend(item)
        print("Extended the list with [{}] items".format(len(item)))

    def remove(self, item):
        super().remove(item)
        print("Removed [{}] from the list.".format(item))

    def pop(self, index=-1):
        item = super().pop(index)
        print("Popped [{}] from the list.".format(item))
        return item
