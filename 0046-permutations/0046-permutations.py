class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def generate(A = []):
            if len(A) == len(nums):
                ans.append([n for n in A])
            else:
                for n in nums:
                    if n not in A:
                        A.append(n)
                        generate(A)
                        A.pop()

        ans = []
        generate()
        return ans