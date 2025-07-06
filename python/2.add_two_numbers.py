class Node:
    def __init__(self, data, n=None) -> None:
        self.data = data
        self.next_node = n

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data


node1 = Node(2)
node2 = Node(4)
node1.set_next(node2.get_data())
print(node1.get_data())
print(node1.get_next())


class ListNode:
    def __init__(self) -> None:
        pass


# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2:ListNode) -> ListNode:
