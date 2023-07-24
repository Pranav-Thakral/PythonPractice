a=int(input("enter the first no.\n"))
b=int(input("enter the second no.\n"))
c=int(input("enter the third no.\n"))
d=int(input("enter the fourth no.\n"))
if(a>b and a>c and a>d):
    print(a)
elif(b>a and b>c and b>d):
    print(b)
elif(c>a and c>b and c>d):
    print(c)
else:
    print(d)