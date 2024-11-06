class Solution:
    def calculate(self, s: str) -> int:
        curr=0
        result=0
        sign=1
        stack=[]

        for value in s:
            if value == ' ':
                continue
            
            if '0' <= value and value <= '9':
                curr = curr*10 + int(value)

            elif value == '+':
                result += (curr * sign) # result = result + (curr * sign)
                sign = 1 
                curr = 0

            # value is -
            elif value == '-':
                result += (curr * sign) # result = result + (curr * sign)
                sign = -1
                curr = 0
            
            # value is (
            elif value == '(':
                stack.append(result)
                stack.append(sign)
                curr = 0
                result = 0
                sign = 1

            # value is )
            elif value == ')':
                result += (curr * sign) # result = result + (curr * sign)
                result *= stack.pop() # result = result * stack.pop()
                result += stack.pop() # result = result + stack.pop()
                curr = 0
        
        result += (curr * sign)
        return result