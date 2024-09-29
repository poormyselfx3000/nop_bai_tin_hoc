
file11a5inp = open("11a5.inp", encoding = "utf8")

doc11a5 = file11a5inp.read()

names = doc11a5.split(", ")

lastname=None
lastname_list = []
link_name = {}
xongroihehe = []
chuoiten = ""
for temp in names:
    
    name = temp.split()
    
    for tempoftemp in name: # co the thay the bang name[-1] tự nhiên nhấn thử ai zè đc hh
        lastname = tempoftemp
    link_name[lastname] = temp
    lastname_list.append(lastname)
    
lastname_list.sort()

for temp in lastname_list:
   xongroihehe.append(link_name[temp])

for temp in xongroihehe:
    if temp == xongroihehe[-1]:
        chuoiten += f"{temp} "
    else :
        chuoiten += f"{temp}; "


viet = open("ketqua.ketqua","w", encoding = "utf8")
viet.write(chuoiten)

