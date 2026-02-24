import random

so_lan = 10000
thang_giu = 0
thang_doi = 0

for _ in range(so_lan):
    # 0 = dê, 1 = xe
    cua = [0, 0, 1]
    random.shuffle(cua)

    # Người chơi chọn ngẫu nhiên 1 cửa
    chon = random.randint(0, 2)

    # MC mở 1 cửa có dê và không phải cửa đã chọn
    for i in range(3):
        if i != chon and cua[i] == 0:
            cua_mo = i
            break

    # Cửa còn lại chưa mở
    cua_con_lai = [i for i in range(3) if i != chon and i != cua_mo][0]

    # Chiến lược giữ nguyên
    if cua[chon] == 1:
        thang_giu += 1

    # Chiến lược đổi cửa
    if cua[cua_con_lai] == 1:
        thang_doi += 1

print("Tỷ lệ thắng khi GIỮ NGUYÊN:", thang_giu / so_lan)
print("Tỷ lệ thắng khi ĐỔI CỬA:", thang_doi / so_lan)