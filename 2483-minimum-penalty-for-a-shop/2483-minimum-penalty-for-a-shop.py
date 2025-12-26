class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty=0
        j=0
        for i in range(len(customers)):
            if customers[i]=='Y':
                penalty+=1
        
        j=(-1,penalty)
        for i in range(len(customers)):
            if customers[i]=='Y':
                penalty-=1
            else:
                penalty+=1
            if penalty<j[1]:
                j=(i,penalty)
        
        return j[0]+1
