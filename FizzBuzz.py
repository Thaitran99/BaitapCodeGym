# Nhập 2 số trong khoảng
while True :
    str1 = input("Nhập hai số bất kỳ")
    arr1 = str1.split( )
    num_begin = int(arr1[0])
    num_end = int (arr1[1])
    if num_begin >= num_end:
        print("Số kết thúc cần lớn hơn số bắt đầu")
        continue
    else:
        break
for i in range (num_begin,num_end+1):
    if (i % 3  ==0 and i % 5 ==0):        
        print("FizzBuzz")
        continue
    elif i % 3 == 0 :
        print("Fizz")
        continue
    elif i % 5 == 0 :
        print("Buzz")
        continue
    else:
        print(i)
         