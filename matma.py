
# Đọc dữ liệu
f = open("C:\\Users\\PC\\Desktop\\hsg\\MATMA.INP")
K = int(f.readline())
f.close()

danh_sach = []

# Duyệt các số có 3 chữ số
for so in range(100, 1000):
    hang_tram = so // 100
    hang_chuc = (so // 10) % 10
    hang_don_vi = so % 10

    # Điều kiện 1: hàng trăm chẵn
    if hang_tram % 2 != 0:
        continue

    # Điều kiện 2: hàng đơn vị > hàng chục
    if hang_don_vi <= hang_chuc:
        continue

    # Điều kiện 3: tổng chữ số là số nguyên tố
    tong = hang_tram + hang_chuc + hang_don_vi
    if not la_so_nguyen_to(tong):
        continue

    danh_sach.append(so)

# Sắp xếp giảm dần
danh_sach.sort(reverse=True)

# Ghi kết quả
f = open("C:\\Users\\PC\\Desktop\\hsg\\MATMA.OUT", "w")
if len(danh_sach) < K:
    f.write("-1")
else:
    f.write(str(danh_sach[K - 1]))
f.close()

