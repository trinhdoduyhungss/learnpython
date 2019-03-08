import random
tuoi = [12,18,20,21,10]
mang = ['Dần', 'Sửu', 'Tý', 'Hợi', 'Tuất', 'Dậu', 'Thân', 'Mùi', 'Ngọ', 'Tỵ', 'Thìn', 'Mẹo']
ten = ['Bá Đạo','Lê Zăn Đạt', 'Quỳnh Búp Bê','Mèo']
nghe =['giang hồ','buôn muối','thông chốt','Bán đào']

rantuoi = random.choice(tuoi)
ranten = random.choice(ten)
rannghe = random.choice(nghe)
setmang = mang[mang.index('Hợi')-rantuoi % len(mang)]
introduce = 'Ta là %s , làm nghề %s, năm nay ta %s tuổi, cầm mạng con %s,  solo 1 vs 1 vs ta hem :V' %(ranten,rannghe,rantuoi,setmang);

print(introduce)