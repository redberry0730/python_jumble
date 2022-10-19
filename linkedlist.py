class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: [ListNode]) -> [ListNode]:
        total = 0
        temp = head
        while head:
            head = head.next
            total += 1
        total = total//2
        for i in range(total):
            temp = temp.next
        return temp

