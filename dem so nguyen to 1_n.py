import math
n= int(input('n='))
t= 0
for j in range(1, n+1):
    if j ==1:
        continue
    result = True
    for i in range(2,int(math.sqrt(j))+1):
        if j %i ==0:
            result = False
            break
    if(result == True):
        t+=1
print(f"co {t} so nguyen to trong [1, {n}]")
