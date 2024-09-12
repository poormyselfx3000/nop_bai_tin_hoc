# Cho xâu S tối đa 255 ký tự gồm các chữ cái, chữ số và dấu cách. 
# Hãy đếm xem xâu S có bao nhiêu từ (một từ là một hoặc nhiều kí tự viết liền nhau).

s = str(input("hay nhap xau S (toi da 255 ky tu): "))
if len(s) > 255 :
    print("da qua 255 ky tu roi")
else:    
    ktr_xau = []
    tempoftemp = ""
    for temp in s:
        if temp == " ":
            ktr_xau.append(tempoftemp)
            tempoftemp = ''
        else:
            tempoftemp += temp

    ktr_xau.append(tempoftemp)
    print(len(ktr_xau))