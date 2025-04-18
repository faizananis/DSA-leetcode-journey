class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s=set()
        for num in arr:
            if num*2 in s or (num//2 in s and num%2==0):
                return True
            s.add(num)
        return False