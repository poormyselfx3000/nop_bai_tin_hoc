def vietfile(filecanviet, giatricanviet):
    #mo file dau ra
    
    vietancom = open(filecanviet,"w",encoding = "utf8")

    #viet nhung j co trong doc vao file ancom.out  
            
    vietancom.write(giatricanviet)

#hoc inp out lol
def docfile(filecandoc):
    #dung de mo file kia va doc xem trong day co j 

    readancom = open(filecandoc, encoding = "utf8")

    #chuyen du lieu doc duoc qua doc

    doc = readancom.read()
    return doc
