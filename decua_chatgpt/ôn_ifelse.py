# Nhập một số nguyên dương từ người dùng.
# Nếu số đó là số nguyên tố, in ra "Số X là số nguyên tố".
# Nếu không, in ra "Số X không phải là số nguyên tố".

import math


x = int(input("Hãy nhập một số:\n"))

# Kiểm tra nếu x < 2
if x < 2:
    print("Số", x, "không phải là số nguyên tố")
else:
    # Giả định ban đầu x là số nguyên tố
    is_prime = True
    
    # Kiểm tra xem x có chia hết cho số nào từ 2 đến căn bậc hai của x không
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            is_prime = False
            break

    if is_prime:
        print("\nSố", x, "là số nguyên tố")
    else:
        print("\nSố", x, "không phải là số nguyên tố")
