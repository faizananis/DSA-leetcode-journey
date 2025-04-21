class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # i, j = 0, 0
        # n = len(fruits)
        # while j < n and fruits[i] == fruits[j]:
        #     j += 1
        # if j == n:
        #     return n

        # l, r = i, j + 1
        # ans = 0
        # while r < n:
        #     if fruits[r] != fruits[j]:
        #         if fruits[r] == fruits[i]:
        #             i = j
        #             j = r
        #         else:
        #             ans = max(ans, r - l)
        #             i = j
        #             l = j
        #             j = r
        #     r += 1
        # ans = max(ans, r - l)
        # return ans
        left=0
        maxlength=0
        table={}
        for right in range(len(fruits)):
            if fruits[right] not in table:
                table[fruits[right]]=1
            else:
                table[fruits[right]]+=1
            if len(table)<=2:
                maxlength=max(maxlength,right-left+1)
            else:
                table[fruits[left]]-=1
                if table[fruits[left]]==0:
                    table.pop(fruits[left])
                left+=1
        return maxlength
            
            
                

