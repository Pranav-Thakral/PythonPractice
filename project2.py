#randomly select 10 names of students and asiign them random marks(between 45 and 100), calculate their grade and print a dictionary containing these values
import random
students=('emma','siliva','hanah','john','kim','martha','kevin','bob','marry','ben','alex','tim','don','ken','roger')
name=random.sample(students,10)
print(name)
marks=[random.randint(45,100)
      for i in range(10)]
       
print(marks)
def grade(x):
   
        if x<50:
            return ("Grade E")
        elif (x>=50) & (x<65):
            return("Grade D")
        elif (x>=65) & (x<75):
            return("Grade C")
        elif (75<=x) & (x<85):
            return("Grade B")
        elif (85<=x) & (x<95):
            return("Grade A")
        else:
            return("Grade A+")
        
grades=[grade(i) for i in marks]
print(grades)

temp=list(zip(marks,grades))
print(temp)
