# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import itertools


def right(p):
    stack = []
    if len(p) == 0:
        return p
    stack.append(p[0])
    for part in range(1, len(p)):
        if len(stack) == 0 or (stack[-1] == '(' and p[part] == '(') or stack[-1] == ')':
            stack.append(p[part])
        else:
            stack.pop()
    #print(stack)
    return len(stack) == 0

def balanced(p):
    check = 0
    for part in p:
        if part == '(':
            check += 1
        else:
            check -= 1

    if check == 0:
        return True
    else:
        return False

def backwards(p):
    answer = ''
    if len(p) == 0:
        return p
    for i in range(len(p)-1, -1, -1):
        if p[i] == '(':
            answer = ')' + answer
        else:
            answer = '(' + answer
    return answer

def solution(p):
    answer = ''
    u = ''
    v = ''
    if len(p) == 0 or right(p):
        return p

    for i in range(2, len(p)+1, 2):
        #print("why?")
        if balanced(p[0:i]):
            u = p[0:i]
            v = p[i:len(p)]
            break
    print(u + "hi!!" + v)
    if right(u):
        print(u + "right version")
        answer = u + solution(v)
    else:
        print(u + "and" + v)
        print(u[1:len(u)-1])
        answer = '('+solution(v)+')' + backwards(u[1:len(u)-1])
        print(answer)
    return answer

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    p = "()))((()"
    print(solution(p))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
