import random
def mem ():
    name_victim = ['Lan Sục',
                   'Hùng Trọc',
                   'Hải Bay',
                   'Khá Bảnh',
                   'Quỳnh Mèo',
                   'Zê Zăn Zạt',
                   'Zin',
                   'Zông Bương Zất Zại',
                   'Aki',
                   'Tomi',
                   'Zăng Zăng',
                   'Alice',
                   'Emily',
                   'Mary',
                   'Julia',
                   'John',
                   'Jane',
                   'Kumo',
                   'Toru',
                   'Hama',
                   'Machiko',
                   'Mineko',
                   'Umi',
                   'Nyoko',
                   'Rinjin',
                   'Ruri',
                   'Kano',
                   'Kisame',
                   'KIDO',
                   'Gwatan',
                   'Toru']

    membership = []
    gen_ran = ['nam', 'nữ', 'động vật']
    for item in range(len(name_victim)) :
        specie = random.choice(gen_ran)
        age = random.randint(1, 100)
        membership.append((name_victim[item], age, specie))
    return membership


