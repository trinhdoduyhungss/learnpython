#các biến trục oxy xác định hình
ncanh = int(input("Nhập số cạnh:"))
x = int(input("Nhập độ dài x:"));
y = int(input("Nhập độ dài y:"));
o = int(input("Nhập vị trí y:"));
#d : là điểm giao giữa đường thẳng song song y giao với đường thẳng song song với x
d = int(input("Nhập vị trí đường thẳng song song y giao với đường thẳng song song với x:"));
#vẽ tam giác cân
if o*2==x  and o!=0 and d*2==x and ncanh==3 :
        for i in range(x):
            for daucach in range(x-i,0, -1):
                print(' ', end="")
            for dausao in range(0, i*2+1,1):
                print('*',end="")
            print()
#vẽ tam giác vuông trái
if o==0 and y==x and d==0 and ncanh==3:
    for coty in range(x):
        for cotx in range(coty):
            print('*', end=" ")
        print()
#vẽ tam giác vuông phải
if o==0 and d==x and ncanh ==3:
    for i in range(x):
        for daucach in range(x - i, 0, -1):
            print(' ', end="")
        for dausao in range(0, i + 1, 1):
            print('*', end="")
        print()
#vẽ hình vuông
if o==0 and y==x and y==x==d and ncanh==4:
    for coty in range(x):
        for cotx in range(x):
            print('*',end=" ")
        print()
#vẽ hình chữ nhật
if o==0 and y!=x and x==d and d!=y and ncanh==4:
    for coty in range(y):
        for cotx in range(x):
            print('*', end=" ")
        print()
