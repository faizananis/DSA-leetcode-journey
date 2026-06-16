class Solution:
    def processStr(self, s: str) -> str:
        result=[]
        for c in s:
            if c == '*':
                if len(result):
                    result.pop()
            elif c == '#':
                for i in range(len(result)):
                    result.append(result[i])
            elif c == '%':
                if len(result):
                    result.reverse()
            else:
                result.append(c)
        return "".join(result)
            
            