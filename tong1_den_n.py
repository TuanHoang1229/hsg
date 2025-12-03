n = int(input())
if n < 1:
        print("khong hop le")
else:
    t = 0
    for i in range(1,n+1):
        if i % 2 == 0:
            t += i
    print(t)
 
