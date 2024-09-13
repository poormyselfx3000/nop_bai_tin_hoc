# Nhập số nguyên dương n từ người dùng.
# Tính và in ra giá trị của n! (n giai thừa).


n = int(input("nhập số n: "))

#tr hop 1 
if n == 1:
    print("1")

elif n == 2:
    print("1 x 2 = 2")

# lặp số lần nhân đến n
else :
    a , b = 1 , 1
    for i in range(1,n+1):
        tich = a * b
        if i == n :
            print(b ,' = ', tich)
        else:
            print(b ,'x', end =" ")
        a , b = tich , b + 1