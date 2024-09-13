# Dữ liệu vào : TONGCS.INP  Một dòng duy nhất chứa xâu S.
# Kết quả : Ghi vào tệp TONGCS.OUT Một dòng duy nhất chứa tổng đã tính được.

def isdigit(so:str):
    if "0" <= so <= "9":
        return True

s = str(input("hay nhap xau S (toi da 255 ky tu): "))
if len(s) > 255 :
    print("chỉ được nhập tối đa 255 ký tự")

else: 
    ktr_xau = []
    tempoftemp = ""
    display = "tổng: "
    for temp in s:
        if isdigit(temp):
            tempoftemp += temp
        else:
            if tempoftemp != "":
                ktr_xau.append(int(tempoftemp))
                display += tempoftemp + " + "
                tempoftemp = ""

    if tempoftemp != "":
        display += tempoftemp + " + "
        ktr_xau.append(int(tempoftemp))

    display = display[:-2] + " = "
    print(display, end = "")
    print(sum(ktr_xau))

