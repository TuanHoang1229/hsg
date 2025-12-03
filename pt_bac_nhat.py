a, b = map(float, input('a, b = ').split(","))
if a == 0 and b == 0:
    print("phuong trinh co vo so nghiem")
elif a == 0 and b != 0:
    print("phuong trinh vo nghiem")
else:
    print("phuong trinh co 1 nghiem x = ",-b/a)
