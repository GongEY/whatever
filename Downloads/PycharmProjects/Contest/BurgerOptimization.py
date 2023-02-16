count1 = int(input())
count2 = count1
temp = []
result = []

while count2 > 0:
        K = int(input())
        gredients = list(map(int, input().split()))
        gredients.sort()
        if K % 2 == 0:
            t = int(K/2-1)
            temp = [i for i in range(t+1)] * 2
        else:
            t = int((K-1)/2-1)
            temp = [i for i in range(t+1)] * 2
            t = int((K-1)/2)
            temp.append(t)
        temp.sort()
        temp_list = []
        for i in range(K):
            temp_list.append(gredients[i]-temp[i])
        min_list = []
        for i in range(K):
            min_list.append(pow((temp_list[i]), 2))
        min_value = 0
        for i in range(K):
            min_value += min_list[i]
        result.append(min_value)
        count2 -= 1

for i in range(count1):
    print("Case #"+str(i+1)+": "+str(result[i]))
