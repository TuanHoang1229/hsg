fi = open("E:\\LUU MÀN HÌNH 17_8_22\\màn hình\\tu tuan\\hsg\\TEST1.txt")
r,c = map(int,fi.readline().split())

l=[]
for i in range(r):
    tam = fi.readline().split()
    tam = list(map(int,tam))
    tam.insert(0,float("-inf"))     #rào bên trái
    tam.insert(r+1,float("-inf"))    #rào bên phải
    l.append(tam)
t= [float("-inf") for _ in range(r+2)] #biến rào đầu đít
l.insert(0,t)   #rào đầu
l.insert(r+2,t) #rào đít

#xử lí
sum = 0
for i in range(1,r+1):
    for j in range(1,c+1):#phía trên ,phía dưới ,bên trái  ,bên phải
        if max(l[i][j],   l[i-1][j]  ,l[i+1][j] ,l[i][j-1] ,l[i][j+1]) == l[i][j]:
            sum+=1
            
with open("E:\\LUU MÀN HÌNH 17_8_22\\màn hình\\tu tuan\\hsg\\TEST1uot.txt","w") as fo:
    fo.write(f"{sum}")
