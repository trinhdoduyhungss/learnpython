import re
tt_ngay = '31/3/2019 ' \
          'ngày 31 tháng 4 năm 2019 ' \
          'hay 32-3-2019'
#Trích xuất ngày, tháng, năm nếu có trong chuỗi trên
match = re.findall(r'(\d{1,2})(?:[/\- ]| tháng )(\d{1,2})(?:[/\-]| năm )(\d{2,4})',tt_ngay)
if match is not None:
    print(match)
    print(len(match))