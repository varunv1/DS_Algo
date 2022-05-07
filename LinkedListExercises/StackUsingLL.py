class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return self.data


class Stack:
    def __init__(self) -> None:
        self.head = None
        self.count = 0

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def pop(self):
        if self.head:
            data = self.head.data
            self.head = self.head.next
            return data
        return None

    def peek(self):
        return self.head.data


stack = Stack()

for i in range(5):
    stack.push(i)
for i in range(5):
    print(stack.pop())
