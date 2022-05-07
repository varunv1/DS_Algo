from itertools import count
from locale import currency


class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return self.data


class CicularLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.next = node
            self.head = node

        self.head.next = self.tail
        self.count += 1

    def size(self):
        return self.count

    def delete(self, data):
        current = self.tail
        prev = self.tail

        while(current == prev or prev != self.head):
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                    self.head.next = self.tail
                else:
                    prev.next = current.next

                self.count -= 1
                return True
            prev = current
            current = current.next
        return False

    def iter(self):
        current = self.tail
        while(current):
            val = current.data
            current = current.next
            yield val


temp = CicularLinkedList()
temp.append(54)
temp.append(12)
for i in range(100):
    temp.append(i)
print(temp.size())
print(temp.head.next is temp.tail)
print('Deletion status', temp.delete(10))

counter = 0
for i in temp.iter():
    print(i)
    counter += 1
    if counter > 1000:
        break
