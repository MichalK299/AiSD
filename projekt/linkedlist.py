from typing import Any


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, value: Any):
        node = Node(value)
        node.next = self.head
        self.head = node

    def append(self, value: Any):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def node(self, at: int) -> Node:
        node = self.head
        for x in range(at):
            node = node.next
        return node

    def insert(self, value: Any, after: Node) -> None:
        node = Node(value)
        node.next = after.next
        after.next = node

    def pop(self) -> Any:
        temp = self.head
        if temp is not None:
            self.head = temp.next
            temp = None
            return

    def remove_last(self):
        temp = self.head
        while temp.next:
            prev = temp
            temp = temp.next
        prev.next = None

    def remove(self, after: Node):
        temp = after.next.next
        after.next = temp

    def len(self):
        length = 0
        temp = self.head
        while temp:
            length += 1
            temp = temp.next
        return length

    def print(self):
        temp = self.head
        while temp:
            if temp.next is None:
                print(temp.data)
            else:
                print(temp.data, "-> ", end="")

            temp = temp.next


class Stack:
    def __init__(self):
        self.storage = LinkedList()

    def push(self, element: Any):
        self.storage.push(element)

    def pop(self) -> Any:
        self.storage.pop()

    def print(self):
        temp = self.storage.head
        while temp:
            if temp.next is None:
                print(temp.data)
            else:
                print(temp.data)
            temp = temp.next

    def len(self):
        length = 0
        temp = self.head
        while temp:
            length += 1
            temp = temp.next
        return length


class Queue:
    def __init__(self):
        self.storage = LinkedList()

    def peek(self):
        return self.storage.head.data

    def enqueue(self, element: Any):
        self.storage.append(element)

    def dequeue(self):
        self.storage.pop()

    def print(self):
        temp = self.storage.head
        while temp:
            if temp.next is None:
                print(temp.data)
            else:
                print(temp.data, ", ", end="")
            temp = temp.next

print("Linked List")
list = LinkedList()
list.push(3)
list.push(5)
list.push('a')
list.insert(2, list.head)
list.append(15)
list.print()
list.pop()
list.remove_last()
list.remove(list.head)
list.print()

stos = Stack()
stos.push(5)
stos.push(15)
stos.push(53)
stos.pop()
stos.push(44)
stos.print()

kolejka = Queue()
kolejka.enqueue('a')
kolejka.enqueue('b')
kolejka.enqueue('c')
print(kolejka.peek())
kolejka.print()
kolejka.dequeue()
print(kolejka.peek())
kolejka.print()

