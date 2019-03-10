print("Nhap so tien:")
umoney = input()
"""moneyconvert = ''
#cách 1
so = {1:'một', 2:'hai', 3:'ba', 4:'bốn', 5:'năm', 6:'sáu', 7:'bảy', 8:'tám', 9:'chín'}
for chuso,tenso in so.items() :
    if str(chuso) in umoney:j
        if umoney.index(str(chuso)) == 0 :
            if len(umoney) == 1:
                moneyconvert += tenso + ' '
            elif len(umoney) == 3 :
                moneyconvert += tenso + ' trăm '
            elif len(umoney) == 4 :
                moneyconvert += tenso + ' nghìn '
            elif len(umoney) == 5 :
                moneyconvert += tenso + ' chục nghìn '
        if umoney.index(str(chuso)) == 1:
            if len(umoney) == 2:
                moneyconvert += tenso
            elif len(umoney) == 3:
                moneyconvert += tenso + ' mươi '
            elif len(umoney) == 4:
                moneyconvert += tenso + ' trăm '
            elif len(umoney) == 5 :
                moneyconvert += tenso + ' nghìn '
        if umoney.index(str(chuso)) == 2:
            if len(umoney) == 3:
                moneyconvert += tenso
            elif len(umoney) == 4:
                moneyconvert += tenso + ' mươi '
            elif len(umoney) == 5 :
                moneyconvert += tenso + ' trăm '
        if umoney.index(str(chuso)) == 3:
            if len(umoney) == 4:
                moneyconvert += tenso
            elif len(umoney) == 5:
                moneyconvert += tenso + ' mươi '
        if umoney.index(str(chuso)) == 4:
            if len(umoney) == 5:
                moneyconvert += tenso
            elif len(umoney) == 5:
                moneyconvert += tenso + ' mươi '
        if umoney.index(str(chuso)) == 5:
            moneyconvert += tenso +' '
        #tương tự đến n số :V
print(moneyconvert + ' đồng')"""

#cách hai
"""so_tien = umoney

# Xử lý
doc_so = ['Không', 'Một', 'Hai', 'Ba', 'Bốn', 'Năm',
          'Sáu', 'Bảy', 'Tám', 'Chín']"""
doc_vi_tri = ['đồng', 'mười', 'trăm', 'nghìn', 'mươi',
              'trăm', 'triệu', 'mươi', 'trăm', 'tỷ']

"""so_tien_chuoi = str(so_tien)

so_tien_str = ''
for dem, c in enumerate(so_tien_chuoi):
    so_tien_str += doc_so[int(c)] + ' '
    so_tien_str += doc_vi_tri[len(so_tien_chuoi)- dem - 1] + ' '
    #print(c +' '+str(dem)+' '+str(len(so_tien_chuoi)- dem - 1)+' '+str(so_tien_str))
# Làm đẹp
so_tien_str = so_tien_str.replace('Không trăm Không mươi Không đồng', 'đồng chẳn')
so_tien_str = so_tien_str.replace('Không mươi', 'lẻ')

# output
print(so_tien_str)"""
#cách 3
moneyconvert = ''
so = {1:'một', 2:'hai', 3:'ba', 4:'bốn', 5:'năm', 6:'sáu', 7:'bảy', 8:'tám', 9:'chín'}

for chuso,tenso in so.items() :
    if str(chuso) in umoney:
         moneyconvert += tenso + ' ' + doc_vi_tri[len(umoney) - umoney.index(str(chuso)) - 1] + ' '
print(moneyconvert)