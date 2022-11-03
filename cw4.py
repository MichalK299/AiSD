from typing import Any, List
import graphviz

class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, data) -> None:
        self.data = data
        self.children = []

    def is_leaf(self) -> bool:
        if next(self.data) == None:
            return True
        else:
            return False

    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)

    def for_each_deep_first(visit:Callable[['TreeNode'], None]) -> None:

