#expression to calculate sum of n natural numbers using functions
def getSum(num):
  if num == 1:
    return 1
  return num + getSum(num-1)

num = 5
print(getSum(num))
