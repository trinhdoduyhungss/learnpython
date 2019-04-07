import thuvien
# Bai tap 1:
str_path = 'config.txt'
print(thuvien.read(str_path))
print('Number of Line:',thuvien.get_number_of_line(str_path))
print('number of Character:',thuvien.get_number_of_character(str_path))
print('Number of Word',thuvien.get_number_of_word(str_path))
# bai1.write('Hi there!')
# bai1.erase(str_path)