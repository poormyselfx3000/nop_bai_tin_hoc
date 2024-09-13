# Bài 3: In tam giác số
# Viết chương trình để in tam giác số với số hàng n do người dùng nhập vào.

# Yêu cầu:

# Sử dụng vòng lặp for để in tam giác số.
# Mỗi hàng i sẽ có i số từ 1 đến i.
# Ví dụ:

# Nếu n = 4, in ra:
# 1
# 12
# 123
# 1234

n = int(input("nhap so n"))
for i in range(1, n + 1):
    for temp in range(1, i + 1):
        print(temp, end= " ")
    print()