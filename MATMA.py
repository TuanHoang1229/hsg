fi = open("MATMA.INP")
k = int(fi.readline())
kq = -1
def isprime(n):
    check = True
    if n<2: check = False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0: check = False
    return check

for i in range(k+1,1000):
    a = i//100
    b = (i//10)%10
    c = i % 10

    if a % 2==0 and b<c and isprime(a+b+c):
        kq = i
        break

fo = open("MATMA.OUT" , "w")
fo.write(str(kq))

