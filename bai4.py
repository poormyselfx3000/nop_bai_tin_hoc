# Cho một xâu  có không quá  kí tự các chữ cái in thường từ  đến . Tìm kí tự xuất hiện nhiều nhất trong xâu S, nếu có nhiều kí tự xuất hiện nhiều nhất bằng nhau thì in ra theo thứ tự từ điển.
# Dữ liệu vào từ file văn bản KYTU.INP :
# Gồm một xâu S.
# Kết quả ghi ra file văn bản KYTU.OUT:
# In ra kí tự thoả mãn đề bài. Nếu có nhiều kí tự, mỗi kí tự cách nhau một dấu cách.


# danhsach = ["a"]
# danhsach[0]

# danhsachtu = {
#     "a": "a"
# }
# # gan gia tri
# danhsachtu["a"] = 0

# # kiem tra ton tai
# a_co_ton_tai_trong_danhsachtu_hay_khong_nhi = "b" in danhsachtu

# # truy cap du lieu aabc
# giatri = danhsachtu["a"]

# print(giatri)

# danhsach = ["a"]
# danhsach[0]

chuoi = "aabbcc"

tudien = {}

for kitu in chuoi:
    if kitu not in tudien:
        tudien[kitu] = 1
    else:
        tudien[kitu] += 1

top_kitu_xh = []
kitu_counter = 0


for kitu in tudien:
    if tudien[kitu] > kitu_counter:
        kitu_counter = tudien[kitu]
        top_kitu_xh.clear()
        top_kitu_xh.append(kitu)

    elif tudien[kitu] == kitu_counter:
        kitu_counter = tudien[kitu]
        top_kitu_xh.append(kitu)


print(sorted(top_kitu_xh))