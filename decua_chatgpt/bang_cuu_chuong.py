# Sử dụng hai vòng lặp for để in bảng cửu chương.
# Mỗi dòng của bảng cửu chương sẽ chứa các phép nhân từ 1 đến 9.

for i in range(1, 10):
    for itwo in range(1, 10):
        tich = i * itwo
        print(i,' x ',itwo,' = ',tich, end= ", ")
    print("\n")

    