class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.left_child = None
        self.right_child = None

    def __str__(self) -> str:
        return self.data


class Tree:
    def __init__(self) -> None:
        self.root = None
