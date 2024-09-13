# Bài 4: Đảo ngược chuỗi
# Viết chương trình đảo ngược một chuỗi do người dùng nhập vào.

# Yêu cầu:

# Nhập một chuỗi từ người dùng.
# In ra chuỗi đảo ngược.
# Ví dụ:

# Nếu chuỗi nhập vào là "hello", kết quả sẽ là "olleh".

chuoi = str(input("hay nhap vao mot chuoi: "))


i = len(chuoi)
ketqua = ''
for temp in chuoi:
    i -= 1
    ketqua += chuoi[i]
    
print(ketqua)