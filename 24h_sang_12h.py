h = int(input("h =  "))
m = int(input("m =  "))
if h > 23 or m > 59:
    print('gio khong hop le')
else:
    if h == 12:
        print(f'{h}:{m} PM')
    elif h > 12:
        h %= 12
        print(f'{h}:{m} PM')
    else:
        print(f'{h}:{m} AM')
