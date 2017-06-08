# First project euler problem 
def euler_1(n):
  return sum([i * ( (i%3 == 0) + (i%5 == 0) - (i % 15 == 0)) for i in range(n)])
  
assert(euler_1(10) == 23)

print euler_1(1000)
