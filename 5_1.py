from typing import Any, List
import graphviz


class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None

    def isleaf(self) -> bool:
        return not (self.right or self.left)

    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)

    def for_each_level_order(self, data: callable(['TreeNode'])) -> None:
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.for_each_level_order(data)
            elif data > self.data:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.for_each_level_order(data)

    def printtree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

    def printtree2(self):
        print(self.data)


class Tree:
    def __init__(self):
        self.root = None


def main():
    root = TreeNode(27)
    root.add(11)
    root.add(12)
    root.printtree()
    root.printtree2()



if __name__ == "__main__":
    main
