import re
#strss = '[(A,25),18,38,16]' # dùng để kiểm tra xem có chuyển đc qua list ko
strss = '[12,25,18,38,16]'
#kiểm tra
try :
    exec('convert = ' + strss + '\nprint("covert_string : ",convert)')
    exec('str_sort=sorted('+strss+')\nprint("str_sort : ",str_sort)')
except:
    print('False')

print('Hết cách 1\n')
##### một cách khác


# regconize list string
str = "  [12, 25, 38, 18, 16]   " ;

converted_list = re.split('[^0-9]+', str)
converted_list.pop(0)
converted_list.pop(-1)
converted_list = [int(i) for i in converted_list]

print("convert string to list:", converted_list)

print("sort list:", sorted(converted_list))

print('Hết cách 2\n')
##### một cách khác nữa

ttts = str.strip()[1:-1] # xóa ký tự đầu và cuối
cccs = ttts.split(',') # xóa ký tự phẩy
outlist = []
for i in cccs:
    outlist.append(int(i.strip()))
print('outlist : ',outlist)
outlist_sort = sorted(outlist)
print('outlist_sort: ', outlist_sort)

print('Hết cách 3\n')