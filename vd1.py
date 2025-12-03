from time import perf_counter
# b1: doc tep input
fi = open('vd1.inp')
a = int(fi.readline())

#b2: xu ly
def so_nguyen_to(n):
    check = True
    if n<2: check=False
    for i in range(2,int(n**0.5)): #int(n**0.5) la so nguyen can bac 2 cua n
        if n % i == 0: check =False
    return check

def so_nguyen_to2(n):
    if n<=3: return n>1 # 3,2,1,0,-1,...
    if n % 2==0 or n % 3 == 0: return False # 4
    i = 5
    while i < int(n**0.5):
        if n % i == 0 or n % (i+2) == 0: return False
        i+=6
    return True

def so_nguyen_to3(n): # manh nhat
    songuyento =[]
    check = [True]*n
    for i in range(2,n):
        for j in range(i*i,n,i):
            check[j] = False
    for i in range(2,n):
        if check[i]: songuyento.append(i)
    return songuyento
start = perf_counter()
ketqua=[]
# for i in range(2,a):
#     if so_nguyen_to2(i): ketqua.append(i)
print(so_nguyen_to3(a))
end = perf_counter()
print(end - start)

#b3: ghi ra tep out
# fo = open('vd1.out', 'w')
# fo.write(f'{max},{kq}')