
from locale import currency


class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.left_child = None
        self.right_child = None

    def __str__(self) -> str:
        return self.data


class BST:
    def __init__(self) -> None:
        self.head = None
        self.count = 0

    def insert(self, data):
        current = self.head
        node = Node(data)
        self.count += 1
        if current is None:
            print('In none')
            # no node in tree
            self.head = node
            return
        # if there are nodes already in the tree
        while current:
            if data <= current.data:
                if current.left_child is None:
                    current.left_child = node
                    return
                current = current.left_child
            elif data > current.data:
                if current.right_child is None:
                    current.right_child = node
                    return
                current = current.right_child

    def size(self):
        return self.count

    def smallest(self):
        current = self.head
        while(current):
            if current.left_child is None:
                return current.data
            current = current.left_child

    def largest(self):
        current = self.head
        while(current):
            if current.right_child is None:
                return current.data
            current = current.right_child

    def printBST(self):
        current = self.head
        # print(self.head.data)
        while(current):
            print(current.data)
            current = current.left_child


temp = BST()
for i in range(10):
    temp.insert(i)

for i in range(10, 0, -1):
    temp.insert(i)
print(temp.size())
print(temp.smallest())
print(temp.largest())
print(temp.printBST())
