import math
def tri_recursion(k):
  if(k > 0):
    result = math.sqrt(k + tri_recursion(k - 2))
    print(result)
  else:
    result = 0
  return result

print("R-SRAS:") #Recursive Square Root Accumulation Sequence
tri_recursion(20)
