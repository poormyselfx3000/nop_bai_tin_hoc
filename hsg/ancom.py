#viet mot func de tim cac so
# s = None

def tim_so(tim):
    tim = tim.split()
    list_so = []
    for temp in tim:
        list_so.append(int(temp))
    return sum(list_so)

def vietfile(filecanviet, giatricanviet):
    #mo file dau ra
    
    vietancom = open(filecanviet,"w")

    #viet nhung j co trong doc vao file ancom.out  
            
    vietancom.write(giatricanviet)

#hoc inp out lol
def docfile(filecandoc):
    #dung de mo file kia va doc xem trong day co j 

    readancom = open(filecandoc)

    #chuyen du lieu doc duoc qua doc

    doc = readancom.read()
    return doc

print(docfile("C:/Users/vipch/Desktop/caccongthucluonggiac.txt"))
vietfile("chungtacuahientai.timemachine",docfile("C:/Users/vipch/Desktop/caccongthucluonggiac.txt"))


    