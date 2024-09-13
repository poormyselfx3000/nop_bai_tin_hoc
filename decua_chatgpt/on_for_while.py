# Nhập số nguyên dương n từ người dùng.
# Đếm và in ra tổng số các số chia hết cho cả 3 và 5 trong khoảng từ 1 đến n.

n = int(input("Hãy nhập một số nguyên dương:\n"))

count = 0  # Biến đếm số lượng số chia hết cho cả 3 và 5

for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
        count += 1

print(f"Tổng số lượng số chia hết cho cả 3 và 5 từ 1 đến {n} là: {count}")
