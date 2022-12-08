from typing import Any


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
            

class BinarySearchTree:
    root: "BinaryNode"

    def __init__(self, root: "BinaryNode") -> None:
        self.root = root

    def insert(self, value: Any) -> None:
        self.__insert(self.root, value)

    def __insert(self, node: BinaryNode, value: Any) -> BinaryNode:
        while node is not None:
            if node.value > value:
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
        self._remove(self.root, value)

    def _remove(self, node: BinaryNode, value: Any) -> BinaryNode:
        if node.value is None:
            return node
        elif value < node.value:
            node.left_child = self._remove(node.left_child, value)
        elif value > node.value:
            node.right_child = self._remove(node.right_child, value)
        else:
            if node.left_child is None:
                temp = node.left_child
                self.node = None
                return temp
