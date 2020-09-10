# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        mid = curr = head
        counter = 1
        while curr:
            curr = curr.next
            if counter == 2:
                counter = 0
                mid = mid.next
            counter += 1
        return mid
