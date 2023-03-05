import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
dAlpha = ['d', 'l', 'r', 'u']
answer = 'z'

def isValid(nx, ny, n, m):
    return ny > 0 and ny <= m and nx > 0 and nx <= n

def hello(n, m, x, y, r, c, k, depth, tmpStr):
    global answer
    if k < depth + abs(x-r) + abs(y-c):
        return

    if x == r and y == c and k == depth:
        answer = tmpStr
        return
    for i in range(4):
        if isValid(x+dx[i], y+dy[i], n, m) and tmpStr < answer:
            hello(n, m, x + dx[i], y + dy[i], r, c, k, depth + 1, tmpStr + dAlpha[i])

def solution(n, m, x, y, r, c, k):
    dist = abs(x-r) + abs(y -c)
    if dist > k or (k-dist) % 2 == 1:
        return "impossible"
    hello(n, m, x, y, r, c, k, 0, "")

    return answer

if __name__ == '__main__':
    n = 3
    m = 4
    x = 2
    y = 3
    r = 3
    c = 1
    k = 5
    print(solution(n, m, x, y, r, c, k))
