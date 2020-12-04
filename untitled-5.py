def funck1(a,b):
  while a!= 0 and b!= 0:
    if a > b: 
      a = a % b
    else: 
      b = b % a
  return a + b

print (funck1 (700,250))                               