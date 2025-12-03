#Giai thừa n! = 1*2*3*...*n
# n! = n * (n-1)!
def gt(n):
    kq = 1
    for i in range(2,n+1):
        kq *= i
    return kq

def gt2(n):
    f = [0] * (n+1) # khởi tạo list có x ptu = 0
    f[0] = 1
    for i in range(1,n+1):
        f[i] = i * f[i-1]
    return f
x= gt2(10)
print(x[8])
