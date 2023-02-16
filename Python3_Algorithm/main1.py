def solution(cap, n, deliveries, pickups):
    answer = 0
    sum_array_1 = [0] * n
    sum_array_2 = [0] * n
    sum_array_1[n-1] = deliveries[n-1]
    sum_array_2[n-1] = pickups[n-1]
    for i in range(n-2, -1, -1):
        sum_array_1[i] = sum_array_1[i + 1] + deliveries[i]
        sum_array_2[i] = sum_array_2[i + 1] + pickups[i]
    #print(sum_array_1)
    #print(sum_array_2)
    tmp = 0
    visitFrequency = 0
    for i in range(n-1, -1, -1):
        target = max(sum_array_1[i], sum_array_2[i])
        if target > tmp:
            print(target % cap)
            #if target % cap:
                #print("1111")
            #else:
                #print("00000")
            visitFrequency = (target - tmp) // cap + (1 if target % cap else 0)
            answer += (i + 1) * visitFrequency
            tmp += visitFrequency * cap
    return answer*2

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cap = 4
    n = 5
    deliveries = [1, 8, 0, 0, 0]
    pickups = [1, 8, 0, 0, 0]
    print(solution(cap, n, deliveries, pickups))
