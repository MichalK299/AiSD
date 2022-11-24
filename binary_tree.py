from typing import Any, Callable

class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self,value) -> None:
        self.left_child = None
        self.right_child = None
        self.value = value

    def is_leaf(self) -> bool:
        if self.right_child and self.left_child == None:
            return True
        return False

    def add_left_child(self,value) -> None:
        self.left_child = value

    def add_right_child(self, value) -> None:
        self.right_child = value

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child is not None:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child is not None:
            self.right_child.traverse_in_order(visit)
        return

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child is not None:
            self.left_child.traverse_post_order(visit)
        if self.right_child is not None:
            self.right_child.traverse_post_order(visit)
        visit(self)
        return

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        visit(self)
        if self.left_child is not None:
            self.left_child.traverse_pre_order(visit)
        if self.right_child is not None:
            self.right_child.traverse_pre_order(visit)
        return


def print_tree(address:'BinaryNode') -> None:
    if isinstance(address, BinaryNode):
        print(address.value)
    else:
        print(address)

class BinaryTree:
    root: BinaryNode

    def __init__(self, root: "BinaryNode") -> None:
        self.root = root

    def traverse_in_order(self, visit: Callable[[Any], None])->None:
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None])->None:
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None])->None:
        self.root.traverse_post_order(visit)

def main():
    root = BinaryNode(10)
    root.left_child = BinaryNode(9)
    root.right_child = BinaryNode(2)
    root.left_child.left_child = BinaryNode(1)
    root.left_child.right_child = BinaryNode(3)
    root.right_child.left_child = BinaryNode(4)
    root.right_child.right_child = BinaryNode(6)

    print('In order:')
    root.traverse_in_order(print_tree)
    print('Post order:')
    root.traverse_post_order(print_tree)
    print('Pre order:')
    root.traverse_pre_order(print_tree)

if __name__ == "__main__":
    main()
