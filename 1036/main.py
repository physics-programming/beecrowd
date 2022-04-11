import math

A, B, C = map(float, input().split())

delta = B**2 - 4 * A * C
if (delta >= 0) and (A != 0):

    R1 = (-B + math.sqrt(delta) ) / (2 * A)
    R2 = (-B - math.sqrt(delta) ) / (2 * A)

    print(f'R1 = {R1:.5f}')
    print(f'R2 = {R2:.5f}')

else:
    print('Impossivel calcular')
