class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        stack = []  # Monotonically non-ascending stack (to find the Next Smaller Element index)
        res = prices[:]  # Result array to store the discounted prices
        
        for i in range(n - 1, -1, -1):  # Traverse the array from the end
            while stack and prices[stack[-1]] > prices[i]:
                stack.pop()
            
            if stack:
                res[i] -= prices[stack[-1]]
            stack.append(i)
        return res
            
