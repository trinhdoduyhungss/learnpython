import re
tt_mk = 'akj@A#hxyz'
resutls = []
LENGTH = re.compile(r'.{8,}')
CHARACTER = re.compile((r'[!@#$&*]'))
UPPERCASE = re.compile(r'[A-Z]')
LOWERCASE = re.compile(r'[a-z]')
DIGIT = re.compile(r'[0-9]')
ALL_PATTERNS = (LENGTH, CHARACTER, UPPERCASE, LOWERCASE, DIGIT)
def is_password_strong(password):
    for pattern in ALL_PATTERNS :
        r = pattern.findall(password)
        if r is not None and r != []:
            resutls.append(r)


is_password_strong(tt_mk)
if len(resutls) >=3 :
    print("mật khẩu mạnh")
else:
    print("còn yếu")