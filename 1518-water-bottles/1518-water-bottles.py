class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        if numBottles<numExchange:
            return numBottles
        num=numBottles
        count=0
        remain=0
        while num>=numExchange:
            count+=num//numExchange
            remain=num%numExchange
            num//=numExchange
            num+=remain
        return numBottles+count