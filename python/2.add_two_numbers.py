from typing import Optional


class Node:
    def __init__(self, data=0) -> None:
        self.data = data
        self.next: Optional["Node"] = None


class ListNode:
    def __init__(self) -> None:
        self.head = None

    def append_as_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def append_as_first(self, data):
        if self.head is None:
            self.append_as_last(data)
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_first(self):
        if self.head is None:
            return
        self.head = self.head.next

    def delete_last(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next and current.next.next:
            current = current.next
        current.next = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("none")


l1 = ListNode()
l1.append_as_last(9)
l1.append_as_last(9)
l1.append_as_last(9)
l1.append_as_last(9)
l1.append_as_last(9)
l1.append_as_last(9)
l1.append_as_last(9)
l2 = ListNode()
l2.append_as_last(9)
l2.append_as_last(9)
l2.append_as_last(9)
l2.append_as_last(9)


class Solution:
    def lnode_to_num(self, lnode: Optional[ListNode]) -> int:
        my_list = []
        if lnode is None:
            return 0
        current = lnode
        while current:
            my_list.append(str(current.val))
            current = current.next
        my_list = ",".join(my_list)
        my_list = my_list.replace(",", "")
        return int("".join(my_list[::-1]))

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        l1_num = self.lnode_to_num(l1)
        l2_num = self.lnode_to_num(l2)
        l3_num = l1_num + l2_num
        l3_list = []
        l3 = ListNode()
        for num in str(l3_num):
            l3_list.append(int(num))
        for num in l3_list[::-1]:
            l3.append_as_last(num)
        return l3


sol = Solution()
sol.addTwoNumbers(l1, l2)
