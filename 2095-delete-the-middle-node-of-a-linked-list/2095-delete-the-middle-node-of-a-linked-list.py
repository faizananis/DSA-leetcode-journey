# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count=0
        curr=head
        if head.next==None:
            head=None
            return head
        while curr!=None:
            curr=curr.next
            count+=1
        mid=count//2-1
        curr=head
        for i in range(mid):
            curr=curr.next
        if curr.next!=None:
            curr.next=curr.next.next
        return head

        # slow=head
        # fast=head.next
        # while fast!=None:
        #     slow=slow.next
        #     fast=fast.next
        #     if fast!=None:
        #         fast=fast.next
        # if slow.next!=None:
        #     slow.next=slow.next.next
        # else:
        #     head=None
        # return head