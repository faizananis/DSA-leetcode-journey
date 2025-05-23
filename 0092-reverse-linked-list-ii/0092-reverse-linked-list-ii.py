# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # Edge case: no need to reverse
        if left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Step 1: Reach the node just before 'left'
        for _ in range(left - 1):
            prev = prev.next

        # Step 2: Reverse the sublist
        curr = prev.next
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next

        