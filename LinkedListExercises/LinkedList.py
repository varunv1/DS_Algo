class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return self.data


class SinglyLinkedList:
    def __init__(self) -> None:
        self.tail = None
        self.head = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node

        else:
            self.tail = node
            self.head = node
        self.size += 1

# the below method will yield a value when called
# so we can iterate easily

    def iter(self):
        current = self.tail
        while(current):
            val = current.data
            current = current.next
            yield val

# this will be called by print fn
# it will print the data

    def __str__(self) -> str:
        current = self.tail
        temp = []
        while(current):
            temp.append(str(current.data))
            current = current.next
        return ' '.join(temp)

    def delete(self, data):
        # we will delete the node whose data matches
        current = self.tail

        prev = self.tail

        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next

    def search(self, data):
        for node in self.iter():
            if node == data:
                return True
        return False

    def clear(self):
        self.head = self.tail = None
        self.size = 0


words = SinglyLinkedList()
for i in range(100):
    words.append(i)

# words.append(24)
# words.append(26)
# words.append(38)
for i in words.iter():
    print(i, sep=',', end=', ')
print()
print(words.size)
# words.delete(99)
print(words)
print(words.search(100))
print(words.search(88))
words.clear()
print(words.size)
