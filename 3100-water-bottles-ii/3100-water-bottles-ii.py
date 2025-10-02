class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        num=numBottles
        count=0
        while num>0:
            num-=numExchange
            if num>=0:
                count+=1
                num+=1
            numExchange+=1
        return numBottles+count
            
