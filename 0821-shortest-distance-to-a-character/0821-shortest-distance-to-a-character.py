class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        left=-1
        right=-1
        nums=[0]*len(s)

        for i in range(len(s)):
            if s[i]==c:
                left=i
                right=i
                break
            
        for i in range(len(s)):
            if s[i]==c and left!=i:
                right=i
                break

        for i in range(len(s)):
            if i==right:
                left=right
                for j in range(right+1,len(s)):
                    if s[j]==c:
                        right=j
                        break
        
            nums[i]=min(abs(i-left),abs(right-i))
        return nums
