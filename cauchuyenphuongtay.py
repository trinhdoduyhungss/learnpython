import datamember_cauchuyenphuongtay
import math
import random

victims = datamember_cauchuyenphuongtay.mem()
info_victim_xuong_truoc =''
sapxep_victims = sorted(victims, key=lambda tup:tup[1])
sapxep_victims2 = sorted(victims, key=lambda tup:tup[1])
ds_tuoi_victim = []
done_victim = []
quyet_dinh_so_phan = []

for idx,tup in enumerate(sapxep_victims):
    if tup[2] == "chó":
        sapxep_victims.remove(tup)
        # print(len(v))
        sapxep_victims.append(tup)
    if tup[2] == "nam":
        sapxep_victims.remove(tup)
        # print(len(v))
        sapxep_victims.append(tup)
    ds_tuoi_victim.append(tup[1])

for i in ds_tuoi_victim: #Lọc các người có tuổi bị trùng
    for item in sapxep_victims2:
        if ds_tuoi_victim.count(i) >= 2:
            if item[1] == i:
                sapxep_victims2.remove(item)
done_victim = sapxep_victims2

for x in done_victim: #Thành viên còn ở lại
    for item2 in sapxep_victims:
        if x[0] == item2[0]:
            sapxep_victims.remove(item2)

so_thuyen_da_dung = str(math.floor(len(done_victim)/3))# Có 9 tàu cứu hộ tổng cộng, mỗi tàu chỉ chở được 3 người :V

so_thuyen_con_lai = 9 - int(so_thuyen_da_dung)

so_nguoi_xuong_trc = str(len(done_victim))

so_nguoi_o_lai = str(len(sapxep_victims))

for info in done_victim:
    info_victim_xuong_truoc += info[0] +" "+info[2]+" "+str(info[1])+" tuổi, "

if int(so_thuyen_da_dung) < 9:
    truyen_part1 = 'Trong lúc tai nạn đang diễn ra, thuyền trưởng Smith đã nhanh chóng sắp xếp và phân loại hành khách, ông đã chọn ra được %s người xuống dùng %s thuyền cứu hộ chèo ra xa con tàu đang dần đắm chìm xuống lòng đại dương lạnh lẽo, bao gồm những người %s họ thật may mắn khi được ông trao cơ hội thoát đại nạn. Nhưng thuyền trưởng Smith vẫn còn phải giải quyết %s người còn lại trên boong.'%(so_nguoi_xuong_trc, so_thuyen_da_dung,info_victim_xuong_truoc, so_nguoi_o_lai)
    print(truyen_part1)
    for i in range(so_thuyen_con_lai*3):
        v = random.choice(sapxep_victims)
        quyet_dinh_so_phan.append(v)
    truyen_part2 = 'Sau một hồi lựa chọn ngẫu nhiên, ông đã chọn ra %s người nữa được có cơ hội sống khi dùng %s thuyền cứu hộ còn lại. Ông đứng trên boong và ngó mắt xa xa về phía họ, cầu mong họ vượt qua chốn nhọc nhằn.'%(str(len(quyet_dinh_so_phan)), str(so_thuyen_con_lai))
    print(truyen_part2)
else:
    truyen_part = 'Trong lúc tai nạn đang diễn ra, thuyền trưởng Smith đã nhanh chóng sắp xếp và phân loại hành khách, ông đã chọn ra được %s người xuống dùng %s thuyền cứu hộ, bao gồm những người %s họ thật may mắn khi được ông trao cơ hội thoát đại nạn. Vì đã hết thuyền cứu hộ, nên ông đành phải ở đúng cùng %s còn lại trên boong, có lẽ ông sẽ cầu nguyện chờ phép lạ đến với mình và những người khác hoặc cũng ông đành vĩnh biệt cuộc đời khi đã tài cùng sức kiệt, an xuôi theo số phận trời định nhưng cũng có thể ông sẽ kiếm cách xoay sở khác để cứu mình và cứu hành khách'%(so_nguoi_xuong_trc, so_thuyen_da_dung,info_victim_xuong_truoc, so_nguoi_o_lai)
    print(truyen_part)
