def hello(miro, x, y, r, c, k, depth, tmpStr, answer):
    # print(k, depth)
    # print(x, y)
    # print(tmpStr)
    # print(answer)
    # answer.sort()
    # print(answer)
    if x == r and y == c and k == depth:
        return True
    elif k == depth:
        return False
    else:
        tmpStr.append("l")
        if y - 1 > 0:
            tmp = hello(miro, x, y - 1, r, c, k, depth + 1, tmpStr, answer)
        else:
            tmp = False
        if not tmp:
            tmpStr.pop()
        else:
            answer.append(''.join(tmpStr))
            tmpStr.pop()

        # print("l end!!")
        tmpStr.append("r")
        if y + 1 <= len(miro):
            tmp = hello(miro, x, y + 1, r, c, k, depth + 1, tmpStr, answer)
        else:
            tmp = False
        if not tmp:
            tmpStr.pop()
        else:
            answer.append(''.join(tmpStr))
            tmpStr.pop()

        # print("r end!!")
        tmpStr.append("u")
        if x - 1 > 0:
            tmp = hello(miro, x - 1, y, r, c, k, depth + 1, tmpStr, answer)
        else:
            tmp = False
        if not tmp:
            tmpStr.pop()
        else:
            answer.append(''.join(tmpStr))
            tmpStr.pop()

        # print("u end!!")
        tmpStr.append("d")
        if x + 1 <= len(miro[0]):
            tmp = hello(miro, x + 1, y, r, c, k, depth + 1, tmpStr, answer)
        else:
            tmp = False
        if not tmp:
            tmpStr.pop()
        else:
            answer.append(''.join(tmpStr))
            tmpStr.pop()

        # print("everything end!!")
        # print(tmpStr)
        if len(tmpStr) == 0:
            return answer
        else:
            return False


def solution(n, m, x, y, r, c, k):
    answer = []
    miro = [["." for _ in range(n)] for _ in range(m)]
    miro[x - 1][y - 1] = "S"
    miro[r - 1][c - 1] = "E"
    depth = 0
    tmpStr = []
    # print(len(miro[0]), len(miro))
    answer = hello(miro, x, y, r, c, k, depth, tmpStr, answer)
    answer.sort()
    # print(answer)
    if len(answer) == 0:
        return "impossible"
    else:
        return answer[0]

if __name__ == '__main__':
    n = 3
    m = 3
    x = 1
    y = 2
    r = 3
    c = 3
    k = 4
    print(solution(n, m, x, y, r, c, k))
