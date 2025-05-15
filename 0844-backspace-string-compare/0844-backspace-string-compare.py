class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def remove_characters(s):
            stack = []
            for char in s:
                if char == '#' and stack:
                    stack.pop()
                elif char != '#':
                    stack.append(char)
            return stack

        return remove_characters(s) == remove_characters(t)

        # def backspaceCompare(self, S, T):
        #     def back(res, c):
        #         if c != '#': 
        #             res.append(c)
        #         elif res: 
        #             res.pop()
        #         return res
        #     return reduce(back, S, []) == reduce(back, T, [])