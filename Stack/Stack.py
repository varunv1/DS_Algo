from inspect import stack


class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.head = None
        self.count = 0

    def push(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.count += 1

    def pop(self):
        if self.head:
            val = self.head.data
            if self.head.next:
                self.head = self.head.next
            else:
                self.head = None
            self.count -= 1
            return val
        return None

    def peek(self):
        if self.head:
            return self.head.data
        return None

    def size(self):
        return self.count


temp = Stack()
temp.push(21)
for i in range(10):
    temp.push(i)

print(temp.size())
print(temp.pop())
temp.push(100)
print(temp.pop())
print(temp.peek())
print(temp.peek())
