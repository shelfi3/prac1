import math

B = 0
L = 0
R = 1

while R - L > 0.0001:
    fL = L - 1 / (3 + math.sin(3.6 * L)) #значение функции в левой границе
    fR = R - 1 / (3 + math.sin(3.6 * R)) #значение функции в правой границе

    B = L - (fL * (R - L)) / (fR - fL)
    fB = B - 1 / (3 + math.sin(3.6 * B)) #значение функции в точке 

    if fB > 0:
        R = B
    else:
        L = B

    print(B)

print(B)
