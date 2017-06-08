#Does $\pi$ render as math?  No.
#
#Let's define eu1(n) =
def euler_1(n):
  return sum([i * ( (i%3 == 0) + (i%5 == 0) - (i % 15 == 0)) for i in range(n)])
  
print euler_1(10)
print euler_1(1000)
