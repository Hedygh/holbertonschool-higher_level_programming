#!/usr/bin/python3
""" Classe VerboseList """


class VerboseList(list):
    """ Class VerboseList """
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        lgt = len(self)
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(len(self) - lgt))

    def remove(self, item):
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        print("Popped [{}] from the list.".format(self[index]))
        return super().pop(index)
