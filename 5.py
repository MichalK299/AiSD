from typing import Any, List
import graphviz


class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None

    def is_leaf(self) -> bool:
        if next(self.data) == None:
            return True
        return False

    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)

    def for_each_level_order(self, visit: callable(['TreeNode'])) -> None:
        if visit:
            if visit < self.visit:
                if self.left is None:
                    self.left = TreeNode(visit)
                else:
                    self.left.for_each_level_order(visit)
            elif visit > self.visit:
                if self.visit is None:
                    self.right = TreeNode(visit)
                else:
                    self.right.for_each_level_order(visit)
            else:
                self.visit = visit

    def search(self, value: Any):
        if self.value == value:

class Tree:
    def __init__(self):
        self.root = None
