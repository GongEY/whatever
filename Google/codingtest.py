# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    numA = A
    numB = B
    countA = 0
    countB = 0

    if numA == 0:
        while numB > 0:
            print('b')
    elif numB == 0:
        while numA > 0:
            print('a')

    while numA > 0 and numB > 0:
        if numA > 2 and countA < 2:
            countB = 0
            print('a')
            print('a')
            numA -= 2
            countA += 2
        elif numB > 2 and countB < 2:
            countA = 0
            print('b')
            print('b')
            numB -= 2
            countB += 2
        else:  # numA <2 and numB<2
            if countA > countB:
                print('b')
                numB -= 1
            else:
                print('a')
                numA -= 1
    pass
