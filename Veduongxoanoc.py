import turtle
t = turtle.Turtle()
count = 0
d = 1
distance = int(input("Nhập khoảng cách"))
while  count <1000:
    t.forward(d)
    t.left(10)
    count +=1
    if(count %5 ==0) :
         d+=1
    if ( t.xcor() > distance):
        break
       
turtle.done()