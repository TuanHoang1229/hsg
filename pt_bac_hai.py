import math
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a == 0:
    print("khong hop le")
else:
    delta = b**2-4*a*c
    if delta < 0 :
        print('phuon trinh vo nghiem')
    elif delta == 0:
        x = -b/2*a
        print(f"phuong trinh co nghiem kep: x1 = x2 = {x}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"co 2 nghiem: x1 = {x1}, x2 = {x2}")
    
