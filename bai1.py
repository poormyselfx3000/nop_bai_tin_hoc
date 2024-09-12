# Yêu cầu: Tính tổng bình phương của hai số N, M.
# Dữ liệu vào: Từ tệp TONGBP.INP gồm 2 số N, M.
# Kết quả: Ghi vào tệp TONGBP.OUT là tổng bình phương của hai số N, M.

n = int(input("nhap so N"))
m = int(input("nhap so m"))
bp_n = n*n
bp_m = m*m
tong_BP = bp_n + bp_m  
print("Tổng BP: ",n,"^2 + ",m, "^2 = ", bp_n ," + ", bp_m, " = ",tong_BP )
