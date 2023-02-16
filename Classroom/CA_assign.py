import time


start = time.time() #실행시간 체크
a = [0]*101
b = [1]*101
c = [1]*101
d = [1]*101
for i in range(0,101):
    for j in range(0,101):
        a[i] += b[i+j-100]*c[i]
for i in range(0,11):
    for j in range(0,11):
        a[j] += d[i]

end = time.time() #실행시간 체크
print("Finished in %.6f seconds" %(end-start))