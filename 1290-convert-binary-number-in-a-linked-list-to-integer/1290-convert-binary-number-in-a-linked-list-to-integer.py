# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def conversion(self,val):
        i=0
        ans=0
        while val:
            num=val%10
            num*=2**i
            ans+=num
            val//=10
            i+=1
        return ans

    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        num=0
        ptr=head
        while ptr:
            num*=10
            num+=ptr.val
            ptr=ptr.next
        return self.conversion(num)