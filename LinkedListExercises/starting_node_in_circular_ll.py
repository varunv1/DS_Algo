class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return self.data


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def appendItem(self, data):
        current = self.head
        node = Node(data)
        if current:
            while(current.next != None):
                current = current.next
            current.next = node
        else:
            self.head = node

    def printData(self):
        data_list = []
        current = self.head
        while(current):
            data_list.append(current.data)
            current = current.next

        return data_list


temp = LinkedList()
a1 = 3
a2 = 2
a3 = 0
a4 = -4
temp.appendItem()
# print(temp.printData())
