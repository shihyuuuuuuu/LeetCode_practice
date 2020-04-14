# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        length = 1
        tmp = head
        while tmp.next != None:
            tmp = tmp.next
            length += 1
        for i in range(length//2):
            head = head.next
        return head
