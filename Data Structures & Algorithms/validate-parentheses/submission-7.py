class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        key = {')':'(', ']':'[', '}':'{'}
        for i in s:
            if i in key:
                if stack and stack[-1] == key[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return len(stack) == 0