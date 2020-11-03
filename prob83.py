# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head
        while curr:
            if curr.next:
                while curr.val == curr.next.val:
                    curr.next = curr.next.next
                    if not curr.next:
                        break
            curr = curr.next
        return head
