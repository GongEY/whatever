from datetime import datetime

def solution(today, terms, privacies):
    answer = []
    array = {}
    for i in range(len(terms)):
        a, b = terms[i].split(" ")
        b = int(b)
        array[a] = b
    for i in range(len(privacies)):
        c, d = privacies[i].split(" ")
        add = int(array[d])
        year = int(c[0:4])
        month = int(c[5:7]) + add
        day = int(c[8:10]) - 1
        while month > 12:
            month -= 12
            year += 1
        if day == 0:
            month -= 1
            day = 28
        if month == 0:
            year -= 1
            month = 12
        first = datetime(int(today[0:4]), int(today[5:7]), int(today[8:10]))
        second = datetime(year, month, day)
        if first > second:
            answer.append(i + 1)
    return answer