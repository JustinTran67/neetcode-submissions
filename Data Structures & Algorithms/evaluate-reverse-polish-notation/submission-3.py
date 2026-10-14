class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in ("+", "-", "*", "/"):
                y = stack.pop()
                x = stack.pop()
                if i == "+":
                    res = x + y
                elif i == "-":
                    res = x - y
                elif i == "*":
                    res = x * y
                else:
                    res = int(x / y)
                stack.append(res)
            else:
                stack.append(int(i))
        return stack[0]