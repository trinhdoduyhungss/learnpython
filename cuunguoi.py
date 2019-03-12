victims =[('Hùng',18,'nam'),
          ('Lan',23,'nữ'),
          ('Lào',30,'nam'),
          ('Kiều',29,'nữ'),
          ('Tin Tin',8,'chó'),
          ('Uyên',32,'nữ'),
          ('Lan',7,'nữ')]
# cách 1:
r =''
sapxep=''
result = []
for i in range(0,len(victims)):
    if i+1 != len(victims):
        r += str(victims[i][1]) + ','
    else: r += str(victims[i][1])
exec('sapxep=sorted(['+r+'])\nprint(sapxep)')
for item in sapxep:
    for i in range(0, len(victims)):
        if victims[i][1] == item:
            result.append(victims[i])

print(result)#tương tự làm với gender và age giảm dần

#cách 2
get_age =[]
result = []
for i in range(0,len(victims)):
    get_age.append(victims[i][1])
sapxep2 = sorted(get_age)
for item in sapxep:
    for i in range(0, len(victims)):
        if victims[i][1] == item:
            result.append(victims[i])

print(result)#tương tự làm với gender và age giảm dần

#cách 3
sort_by_age = sorted(victims, key=lambda tup:tup[1], reverse=1)
print("\n\nsort theo thứ tự lớn trước nhỏ sau: ")
print(sort_by_age)

v = sorted(victims, key=lambda tup:tup[1])
print("\n\nsort theo thứ tự nhỏ trước lớn sau, rồi mới đên chó:")
for idx,tup in enumerate(v):
    # print(tup)
    if tup[2] == "chó":
        v.remove(tup)
        # print(len(v))
        v.append(tup)
print(v)