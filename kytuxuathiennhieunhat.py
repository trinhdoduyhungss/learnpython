check_string = "Con ngựa đá con ngựa đá. Con ngựa đá không đá con ngựa"
dictword = []
for charss in check_string.strip().split(' '):
    dictword.append((charss,check_string.count(charss)))
result = sorted(dictword, key=lambda word:word[1], reverse=1)
print('từ lặp nhiều nhất : ',result[0][0],', số lần lặp : ', result[0][1])