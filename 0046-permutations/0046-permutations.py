class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def generate(A,arr):
            if len(arr) == len(nums):
                ans.append(arr[:])
            else:
                for i in range(len(nums)):
                    if i not in A:
                        A.append(i)
                        arr.append(nums[i])
                        generate(A,arr)
                        A.pop()
                        arr.pop()

        ans = []
        A=[]
        arr=[]
        generate(A,arr)
        return ans