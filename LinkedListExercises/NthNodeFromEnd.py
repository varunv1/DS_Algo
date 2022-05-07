# optimal solutin
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return self.data


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert(self, data):
        current = self.head
        node = Node(data)
        if current:
            while(current.next):
                current = current.next
            current.next = node
        else:
            self.head = node

    def nth_from_last(self, n):
        # find the nth element from the last
        if n <= 0:
            return
        nth_ptr = self.head
        currnet = self.head
        count = 0
        while count < n and nth_ptr:
            nth_ptr = nth_ptr.next
            count += 1
        if not nth_ptr:
            return 'Less number of elements are present.'
        while(nth_ptr):
            currnet = currnet.next
            nth_ptr = nth_ptr.next
        return currnet.data


temp = LinkedList()
for i in range(10):
    temp.insert(i)
print(temp.nth_from_last(0))
