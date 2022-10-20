from typing import Any


class Node:
    value: Any
    next: 'Node'

    def __init__(self, value: Any) -> None:
        self.value = value


class LinkedList:
    head: Node
    tail: Node

    def __init__(self) -> None:
        self.LinkedList = []
        self.head = None
        self.tail = None

    def push(self, value: Any) -> None:
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def append(self, value: Any) -> None:
        self.LinkedList.append(value)

    def node(self, at: int) -> Node:
        return self.index(at)

    def insert(self, value: Any, after: Node) -> None:
        self.LinkedList.append(after, value)

    def remove_last(self) -> Any:
        return self.LinkedList.pop()

    def remove(self, after: Node) -> Any:
        return self.LinkedList.pop(after)


lista = LinkedList()
lista.push(1)
lista.push(2)
lista.append(3)
print(lista.__dict__)
lista.remove_last()
print(lista.__dict__)

# zadanie 2

class Stack:
    _storage: LinkedList

    def __init__(self) -> None:
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def len(self) -> int:
        return len(self.stack)


stack = Stack()
print(stack.__dict__)

stack.push(3)
stack.push(10)
stack.push(1)
print(stack.__dict__)
print(stack.len())
stack.pop()
print(stack.__dict__)


# zadanie 3


class Queue:
    _storage: LinkedList

    def __init__(self) -> None:
        self.queue = list()

    def peek(self):
        return self.queue[0]

    def enqueue(self, element: Any) -> None:
        self.queue.append(element)

    def dequeue(self) -> Any:
        return self.queue.pop(0)

    def len(self) -> int:
        return len(self.queue)
