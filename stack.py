S = '11++'


def solution(s):
    op = None
    stack = list()
    for c in s:
        if c == '+' or c == '*':
            if len(stack) > 1:
                if c == '+':
                    tmp = stack.pop() + stack.pop()
                    stack.append(tmp)
                else:
                    tmp = stack.pop() * stack.pop()
                    stack.append(tmp)
            else:
                return -1
        else:
            stack.append(int(c))
    return stack[0]




print(solution(S))