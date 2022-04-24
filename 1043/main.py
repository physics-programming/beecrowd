
A, B, C = map(float, input().split())

condition1 = abs(B - C) < A < B + C
condition2 = abs(A - C) < B < A + C
condition3 = abs(A - B) < C < A + B

if condition1 and condition2 and condition3:
    perimetro = A + B + C
    print(f'Perimetro = {perimetro:.1f}')
else:
    area =  (A + B) * C / 2
    print(f'Area = {area:.1f}')