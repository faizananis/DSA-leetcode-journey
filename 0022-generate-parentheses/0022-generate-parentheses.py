# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         count=0
#         size=n*2
#         ans=[]
#         st=""
#         def solve(string,count):
#             if count<0:
#                 string=string[:-1]
#                 return
#             if len(string)>size:
#                 return
#             if len(string)==size and count==0:
#                 ans.append(string)
#                 return
#             string+='('
#             solve(string,count+1)
#             string+=')'
#             solve(string,count-1)
#         solve(st,count)
#         return ans
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current: str, open_used: int, close_used: int):
            # Base case: all brackets used
            if len(current) == 2 * n:
                result.append(current)
                return

            # Try adding an opening bracket
            if open_used < n:
                backtrack(current + "(", open_used + 1, close_used)

            # Try adding a closing bracket only if it won't break validity
            if close_used < open_used:
                backtrack(current + ")", open_used, close_used + 1)

        # Start recursion
        backtrack("", 0, 0)
        return result
            
            
            