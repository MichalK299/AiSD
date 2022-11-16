from typing import Any, List, Callable, Union
import graphviz
from linkedlist import *


class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value: Any) -> None:
        self.value = value
        self.children: List['TreeNode'] = []

    def is_leaf(self) -> bool:
        if len(self.children) == 0:
            return True
        else:
            return False

    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        for x in self.children:
            x.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        fifo: "Queue" = Queue()
        for x in self.children:
            fifo.enqueue(x)

    def search(self, value: Any) -> Union['TreeNode', None]:
        if self.value == value:
            return self
        for x in self.children:
            if x.value == value:
                return self
        return None

    def print(adres:'TreeNode') -> None:
        if isinstance(adres, TreeNode):
            print(adres.value)
        else:
            print(adres)


class Tree:
    def __init__(self, root: "TreeNode") -> None:
        self.root = root

    def add(self, value: Any, parent_name: Any) -> None:
        parent_name.children.append(TreeNode(value))

    def for_each_deep_first(self, visit: Callable[['Tree'], None]) -> None:
        self.root.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['Tree'], None]) -> None:
        self.root.for_each_level_order(visit)


def print_tree(adres:'TreeNode') -> None:
    if isinstance(adres, TreeNode):
        print(adres.value)
    else:
        print(adres)


print("-------")

tree = TreeNode(1)
tree.add(TreeNode(2))
tree.add(TreeNode(3))
tree.add(TreeNode(4))
tree.children[0].add(TreeNode(5))
tree.children[0].add(TreeNode(6))
tree.children[2].add(TreeNode(7))
tree.children[2].add(TreeNode(8))


tree.for_each_deep_first(print_tree)

print("-------")

tree.for_each_level_order(print_tree)
