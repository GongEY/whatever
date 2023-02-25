def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
# 유클리드 호제법을 사용한다
n = int(input())
count = 0
for k in range(1, n, 1):  # 1부터 n-1 인 k에 대하여
    if k > n - k:  # a>b인 경우 패스
        continue
    elif k == n - k:
        count += 1
    elif gcd(k , n - k) != 1:  # 서로소가 아닐 경우 패스
        continue
    else:
        count += 1

print(count)