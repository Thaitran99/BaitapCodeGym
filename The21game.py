import random
current_player = random.randint(0,1)
total = 0
num = 0
while True:
    total += num
    print("** total = ",total)
    if total >=21 :
        break
    else:
        if current_player == 0 :
            print("->human")
            while True:
                num = int(input("Thêm số trong khoảng [1,3]"))
                if num <1 or num >3 :
                    continue
                else:
                    print("-->Human choose",num)
                    break
            current_player =1
            continue     
        if current_player == 1:
            print("->computer")
            num = random.randint(1,3)
            print("-->Computer choose ",num)
            current_player =0
if current_player ==0:
    print("Human win")
else:
    print("Machine win")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
 