class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for ch in s:
            if(len(stack) > 0):
                top = stack[len(stack)-1]
                if(top == '(' and ch == ')'):
                    stack.pop()
                elif(top == '{' and ch == '}'):
                    stack.pop()
                elif(top == '[' and ch == ']'):
                    stack.pop()
                else:
                    stack.append(ch)
            else:
                stack.append(ch)

        return False if len(stack) > 0 else True