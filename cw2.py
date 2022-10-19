from typing import Any


class Node:
    value: Any
    next: 'Node'


class LinkedList:
    head: Node
    tail: Node

class Node:
    value: Any
    next: 'Node'

    def push(self, value: Any) -> None:
        self.node.insert(0, value)

    def append(self, value: Any) -> None:
        self.node.append(value)

    def node(self, at: int) -> Node:
        return self.index(at)

    def insert(self, value: Any, after: Node) -> None:
        self.node.append(after+1, value)

    def remove_last(self) -> Any:
        return self.node.pop()
        
# zadanie 2

class Stack:
    _storage: LinkedList

    def __init__(self):
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


# zadanie 3

class Queue:
    _storage: LinkedList

    def __init__(self):
        self.queue = list()

    def peek(self):
        return self.queue[0]

    def enqueue(self, element: Any) -> None:
        self.queue.append(element)

    def dequeue(self) -> Any:
        return self.queue.pop(0)

    def len(self) -> int:
        return len(self.queue)
