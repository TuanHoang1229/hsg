#f[0] = 0 ; f[1]=1
#f[n]= f[n-1]+f[n-2]

nmax = 1000
def fibo(n):
    f = [0] * (nmax+1) # f[0]=0
    f[1]=1
    for i in range(2,nmax+1):
        f[i]=f[i-1]+f[i-2]
    return f

def fibo2(n):
    tg = 5**(1/2)
    kq = (1/tg)*(((1+tg)/2)**n - ((1-tg)/2)**2)
    return kq

f=fibo(nmax)
print(f[999])
print(fibo2(999))