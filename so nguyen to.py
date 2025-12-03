n= int(input('n='))
if n <1:
    print('khong hop le')
elif n == 1:
    print('1 khong phai so nguen to')
else:
    rs = True
    for i in range(2,n):
        if n % 2 ==0:
            rs = False
            break
    if rs == True:
        print(f'{n} la so nguyen to')
    else:
        print(f'{n} khong phai la so nguyen to')
    
    
