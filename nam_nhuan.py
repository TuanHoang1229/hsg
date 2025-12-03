y = int(input('y ='))
if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
    print(f"{y} la nam nhuan")
elif y < 1582:
    print("khong tinh theo lich gregorius")
else:
    print(f'{y} khong la nam nhuan')
