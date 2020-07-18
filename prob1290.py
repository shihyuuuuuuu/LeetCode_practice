# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        temp = head
        length = ans = 0
        while temp:
            length += 1
            temp = temp.next
        for i in range(length):
            ans += 2**(length-i-1) * head.val
            head = head.next
        return ans
