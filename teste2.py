n = input().split()

A = int(n[0])
B = int(n[1])
C = int(n[2])
D = int(n[3])

somaCD = C + D
somaAB = A + B

if B > C:
    if D > A:
        if somaCD > somaAB:
            if C > 0 and D > 0:
                    if A % 2 == 0:
                         print('Valores aceitos')
                    else:
                        print('Valores nao aceitos')
            else:
                print('Valores nao aceitos')
        else:
            print('Valores nao aceitos')
    else:
        print('Valores nao aceitos')
else:
    print('Valores nao aceitos')