# Cho một xâu  có không quá  kí tự các chữ cái in thường từ  đến . Tìm kí tự xuất hiện nhiều nhất trong xâu S, nếu có nhiều kí tự xuất hiện nhiều nhất bằng nhau thì in ra theo thứ tự từ điển.
# Dữ liệu vào từ file văn bản KYTU.INP :
# Gồm một xâu S.
# Kết quả ghi ra file văn bản KYTU.OUT:
# In ra kí tự thoả mãn đề bài. Nếu có nhiều kí tự, mỗi kí tự cách nhau một dấu cách.


s = str(input("nhap gtr s: "))

tempoftemp = []
ktr_xau = []

for temp in s:
    if not temp in tempoftemp:
        ktr_xau.append(temp)

    tempoftemp.append(temp)
      



