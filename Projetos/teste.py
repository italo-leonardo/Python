n = input().split()

A, B, C = float(n[0]), float(n[1]), float(n[2])


if A + B > C and B + C > A and A + C > B:
    P = A + B + C
    print(f'Perimetro = {P:.1f}')
else:
    Area = ((A + B) * C )/ 2
    print(f'Area = {Area:.1f}')