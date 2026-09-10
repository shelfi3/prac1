
import math

B = 0
L = 0
R = 1


while R - L > 0.0001:

  B = (L + R) / 2

  fB = B-1/(3 + math.sin(3.6 * B)) #значение функции в серединной точке 

  if  fB> 0: 
      R = B
  else:
      L = B

  print( B)

print(B)
