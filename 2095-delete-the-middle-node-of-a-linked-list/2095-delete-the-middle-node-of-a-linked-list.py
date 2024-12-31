# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        slow = head
        fast = head
        if head.next == None:
            return None
        while fast and fast.next:
            prev = slow
            slow  = slow.next
            fast = fast.next.next

        temp=slow
        prev.next = slow.next
        temp.next=None
        return head
        # if head.next==None:
        #     return None
        
        # slow = head
        # fast = head
        
        # while fast and fast.next:
        #     fast = fast.next.next
        #     if fast and fast.next:
        #         slow = slow.next
        
        # slow.next = slow.next.next
        
        # return head
    
    # def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     turtle, hare = head, head
    #     while hare.next and hare.next.next and hare.next.next.next != None:
    #         turtle = turtle.next
    #         hare = hare.next.next
        
    #     if head.next:
    #         temp = turtle.next.next
    #         turtle.next.next = None
    #         turtle.next = temp
    #         return head

        