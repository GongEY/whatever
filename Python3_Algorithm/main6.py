def dfs(bin, index):
    leftLen = index // 2
    rightLen = index - leftLen - 1  # root를 제외하기 때문에 추가로 1을 뺀다
    if leftLen == 0:  # 자식 노드이기 때문에 1이든 0이든 상관없다, 무조건 참
        return 1
    elif bin[leftLen] == "0":  # 루트 노드가 0이면 자식 노드가 모두 0이 아니면 거짓이 된다
        for i in range(index):
            if bin[i] == "1":
                return 0
        return 1
    hi = dfs(bin[:leftLen], leftLen)  # 왼쪽 길이의 노드들이 참인지 탐색한다.
    hello = dfs(bin[leftLen + 1:index], rightLen)  # 오른쪽 길이의 노드들이 참인지 탐색한다.
    if hi == 0 or hello == 0:
        return 0
    else:
        return 1


def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        bin = str(format(numbers[i], 'b'))
        binbin = str(format(len(bin) + 1, 'b'))
        if '1' in binbin[1:]:  # 포화 트리로 만들 수 없다. 100....(2) 의 형태가 아니다!!!
            dummies = int('0b1' + '0' * len(binbin), 2) - int('0b' + binbin, 2)
            bin = "0" * dummies + bin
        # print(bin)
        # if len(bin) % 2 != 1:  # 만약 길이가 짝수면 루트 노드를 구할 수 없으니 앞에 0을 붙인다
        # bin = "0" + bin
        index = len(bin)
        tmp = dfs(bin, index)
        answer.append(tmp)

    return answer

if __name__ == '__main__':
    numbers = [7, 42, 5]
    print(solution(numbers))
