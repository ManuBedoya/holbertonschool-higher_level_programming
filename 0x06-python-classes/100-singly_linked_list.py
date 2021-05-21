#!/usr/bin/python3
"""Module to create 2 classes
"""


class Node:
    """This is a Node class
    """
    def __init__(self, data, next_node=None):
        """This is a __init__ classs
        Is to initianilize the variables
        Args:
           data ()
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')


class SinglyLinkedList:
    """This is a SinglyLinkedList class
    """
    def __init__(self):
        """This is a __init__ function
        Is to initianilize the variables
        """
        self.__head = None

    def __str__(self):
        result = ""
        aux = self.__head
        if self.__head is None:
            return result
        while (aux):
            result += str(aux.data)
            if aux.next_node is not None:
                result += "\n"
            aux = aux.next_node
        return result

    def sorted_insert(self, value):

        new_node = Node(value)
        if not self.__head or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            ant = None
            aux = self.__head

            while(aux):
                if aux.data >= value:
                    new_node.next_node = aux
                    break
                ant = aux
                aux = aux.next_node

            ant.next_node = new_node
