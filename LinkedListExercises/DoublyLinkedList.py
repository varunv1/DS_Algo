class Node:
    def __init__(self, data=None, next=None, prev=None) -> None:
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self) -> str:
        return self.data


class DoublyLinkedList:
    def __init__(self) -> None:
        head = None
        tail = None
        count = 0

    def append(self, data):
        """Append an item to the list"""

        node = Node(data)
        if self.head is None:
            self.tail = node
            self.head = node
        else:
            node.prev = self.head
            self.head.next = node
            self.head = node
        self.count += 1

    def iter(self):
        current = self.tail
        while(current):
            val = current.data
            current = current.next
            yield val

    def delete(self, data):
        current = self.tail
        node_deleted = False
        # if no element is present
        if current is None:
            node_deleted = False
        # taking tale as first node here
        # if the first element is the one
        elif current.data == data:
            current.next.prev = None
            current = current.next
            self.tail = current
            node_deleted = True
        # taking head as last node of the list
        # if the last element is the one
        elif self.head.data == data:
            self.head = self.head.prev
            self.head.next = None
            node_deleted = True
            # look into all the remaining elements
        else:
            while current:
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                current = current.next
        # reduce the cound if deleted the node
        if node_deleted:
            self.count -= 1
        return True

    def contain(self, data):
        for i in self.iter():
            if i.data == data:
                return True
        return False
