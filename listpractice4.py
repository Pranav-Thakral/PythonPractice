number=[100,3,600,900,1000,20,10]
print (number)
min_value=20
max_value=600
for i in range(6,-1,-1):
    if number[i]>min_value and number[i]<max_value:
        del number[i]
        print(number)