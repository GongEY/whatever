# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import itertools


def solution(relation):
    row = len(relation)
    col = len(relation[0])

    combi_array = []
    for i in range(1, col+1):
        combi_array.extend(itertools.combinations(range(col), i))

    print(combi_array)
    # 유일성
    unique = []
    for combi in combi_array:
        tmp = [tuple([item[i] for i in combi])for item in relation]
        if row == len(set(tmp)):
            unique.append(combi)
    print(unique)
    # 최소성
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            # 교집합을 구해서 부분집합이 일치하는 지 확인
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])
    return len(answer)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
    print(solution(relation))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
