a = int (input("Hay nhap so tien"))
if (a<75):
    b = a;
elif ( a<100 and a>=75):
    b = a-15
elif (a<150 and a>=100):
    b = a-20
else :
    b = a-25
print(" So tien can phai tra la ", b)
   