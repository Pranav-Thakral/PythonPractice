def percent(marks):
    percent=((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
    return percent
marks1=[23,45,65,78]
percentage=percent(marks1)

marks2=[98,76,90,88]
percentage2=percent(marks2)
print(percentage,percentage2)

#function practice 2 
def greet(person="stranger"):
    print("good day!"+person)
greet ("pranav ")
def my_sum(num1, num2):
    return num1+num2
sum=my_sum(34,56)
print(sum)
#function practice 3
greet()

