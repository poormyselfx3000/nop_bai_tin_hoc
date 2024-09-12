# Dữ liệu vào : TONGCS.INP  Một dòng duy nhất chứa xâu S.
# Kết quả : Ghi vào tệp TONGCS.OUT Một dòng duy nhất chứa tổng đã tính được.

s = str(input("hay nhap xau S (toi da 255 ky tu): "))
if len(s) > 255 :
    print("chỉ được nhập tối đa 255 ký tự")

else: 
    ktr_xau = []
    tempoftemp = ""
    print("tổng:",end=" ")
    for temp in s:
        if temp.isdigit():
            tempoftemp += temp
        else:
            if tempoftemp != "":
                ktr_xau.append(int(tempoftemp))
                print(tempoftemp, end= " + ")
                tempoftemp = ""

    if tempoftemp != "":
        print(tempoftemp, end= " = ")
        ktr_xau.append(int(tempoftemp))


    print(sum(ktr_xau))
