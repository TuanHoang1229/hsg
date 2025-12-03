n=int(input('n='))
x=float(input('x='))
if n >= 0:
    t=0
    for i in range(0,n+1):
        t = t +x**i
    print(f'f(x)={t}')
