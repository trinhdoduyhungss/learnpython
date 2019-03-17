
# không đệ quy
f0 = 0
f1 = 1
f2 = 0
b  = ""
n = int(input("nhập n:"))
for i in range(n-1):
   f2 = f0 + f1
   b += str(f2)+" "
   f0 = f1
   f1 = f2

print('0 1 '+b)
#dùng đệ quy - kém hiệu quả hơn, chỉ được cái gọn
def fibonacci(n) :
    if n == 0 or n == 1:
        return n
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
        return result

print(fibonacci(n))

