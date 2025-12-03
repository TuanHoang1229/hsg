n= int(input('n='))
if n < 0:
    print('khong hop le')
else:
    t=1
    for i in range(1,n+1):
        t = t*i
    print(f"{n}!={t}")
