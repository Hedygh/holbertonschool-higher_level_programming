#!/usr/bin/python3
""" class Node """


class Node:
    """ Define node in a list """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

""" class SinglyLinkedList """


class SinglyLinkedList:
    """ Defines a singly Linked list """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new = Node(value)
        if self.__head is None:
            self.__head = new
            new.next_node = None
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            head = self.__head
            while (head is not None and
                    head.next_node is not None and
                    head.next_node.data < new.data):
                head = head.next_node
                new.next_node = head.next_node
                head.next_node = new

    def __str__(self):
        """ Make the list a printable object as string """
        head = self.__head
        string = []
        sep = '\n'
        while (head is not None):
            string.append(str(head.data))
            head = head.next_node
        return (sep.join(string))
