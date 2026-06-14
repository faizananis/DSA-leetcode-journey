# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        count=0
        temp=head
        while temp:
            temp=temp.next
            count+=1
        half=count//2
        sums=[0]*half
        temp=head
        for i in range(half):
            sums[i]=temp.val
            temp=temp.next
        for i in range(half):
            sums[half-i-1]+=temp.val
            temp=temp.next
        return max(sums)
