class Solution:
    from typing import List
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        n = len(tokens)
        for i in range(n):
            print(stack , "is stack")
            if tokens[i].isdigit():
                stack.append(int(tokens[i]))
            elif tokens[i][1:].isdigit():
                # print("tokens[1:] is ",tokens[i][1:])
                stack.append(-int(tokens[i][1:]))
            else:
                popper2 = stack.pop()
                popper1 = stack.pop()
                if tokens[i] == '+':
                    stack.append(popper1 + popper2)
                elif tokens[i] == '-':
                    stack.append(popper1 - popper2)
                elif tokens[i] == '*':
                    stack.append(popper1 * popper2)
                elif tokens[i] == '/':
                    stack.append(popper1 // popper2)
        return stack[0]
if __name__ == '__main__':
    Solu = Solution()
    ret = Solu.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
    print(ret)