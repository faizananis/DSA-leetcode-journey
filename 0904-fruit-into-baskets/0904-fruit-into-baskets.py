class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        j=0
        maxlength=0
        table={}
        for i in range(len(fruits)):
            if fruits[i] not in table:
                table[fruits[i]]=1
            else:
                table[fruits[i]]+=1
            if len(table)<=2:
                maxlength=max(maxlength,i-j+1)
            else:
                table[fruits[j]]-=1
                if table[fruits[j]]==0:
                    table.pop(fruits[j])
                j+=1
        return maxlength
            
            
                

