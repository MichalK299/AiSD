from typing import Any
import graphviz


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value: Any) -> None:
        self.value = value
        self.left_child = None
        self.right_child = None

    def min(self) -> "BinaryNode":
        if self.left_child is None:
            return self
        else:
            self.left_child.min()

    def print_tree(self):
        if self.left_child:
            self.left_child.print_tree()
        print(self.value)
        if self.right_child:
            self.right_child.print_tree()


class BinarySearchTree:
    root: "BinaryNode"

    def __init__(self, root: "BinaryNode") -> None:
        self.root = root

    def insert(self, value: Any) -> None:
        self.__insert(self.root, value)

    def __insert(self, node: BinaryNode, value: Any) -> BinaryNode:
        if node is None:
            return BinaryNode(value)
        if value < node.value:
            node.left_child = self.__insert(node.left_child, value)
        else:
            node.right_child = self.__insert(node.right_child, value)
        return node

    def insert_list(self, list_: list[Any]) -> None:
        for x in list_:
            self.insert(x)

    def contains(self, value: Any) -> bool:
        x = self.root
        while x is not None:
            if x.value == value:
                return True
            elif x.value > value:
                x = x.left_child
            else:
                x = x.right_child
        return False

    def remove(self, value: Any) -> None:
        self.__remove(self.root, value)

    def __remove(self, node: BinaryNode, value: Any):
        if node is None:
            return node
        if value == node.value:
            if node.left_child is None:
                node = node.right_child
            elif node.right_child is None:
                node = node.left_child
            else:
                node.right_child = self.__remove(node.right_child, node.value)
        elif value < node.value:
            node.left_child = self.__remove(node.left_child, value)
        else:
            node.right_child = self.__remove(node.right_child, value)
        return node

    def print_tree(self):
        if self.root.left_child:
            self.root.left_child.print_tree()
        print(self.root.value)
        if self.root.right_child:
            self.root.right_child.print_tree()


t = BinarySearchTree(BinaryNode(4))
t.insert(1)
t.insert(5)
t.insert(3)
t.insert(8)
t.insert(10)
t.print_tree()
print(t.contains(6))
print(t.contains(1))

t.remove(6)
t.remove(10)

print('-----------')
t.print_tree()

print(t.contains(6))
print(t.contains(1))
