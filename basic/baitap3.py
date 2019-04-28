import math
congthuc = '√([(2*A*B)/C])'
giatri = [('A',5), ('B',10), ('C',7.5)]
A = giatri[0][1]
B = giatri[1][1]
C = giatri[2][1]
congthucconvert = congthuc.replace('√','')
exec('ketqua = '+congthucconvert+'\nprint(math.sqrt(ketqua[0]))')
#print(congthucconvert)