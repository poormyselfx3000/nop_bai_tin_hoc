# Nhập số n từ người dùng.
# In ra dãy Fibonacci với n phần tử đầu tiên. Dãy Fibonacci là dãy bắt đầu từ 0, 1, và mỗi số tiếp theo bằng tổng của hai số trước đó.

n = int(input("Nhập số n: "))

if n == 1:
    print(0)
elif n == 2:
    print(0, 1)
else:
    a, b = 0, 1
    print(a, b, end=" ")

    for i in range(2, n):
        fib = a + b
        print(fib, end=" ")
        a, b = b, fib


