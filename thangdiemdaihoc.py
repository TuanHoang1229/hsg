gpa4 = float(input("GPA(4) = "))
gpa10 = (gpa4*10)/4
if gpa4 <= 4 and gpa4 >= 0:
    print(f'GPA(10) = {gpa10}')
elif gpa4 < 0 :
    print('khong thoa man')
else:
    print("khong thoa man")
