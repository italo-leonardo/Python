'''num = [[],[], []]
for i in range(0, 3):
    num[0].append(int(input(f'Digite um valor para: [0, {i}]: ')))
for i in range(0, 3):
    num[1].append(int(input(f'Digite um valor para: [1, {i}]: ')))
for i in range(0, 3):
    num[2].append(int(input(f'Digite um valor para: [2, {i}]: ')))
print(num)
for i in num[0]:
    print(f'[{i}]', end='')
print()
for i in num[1]:
    print(f'[{i}]', end='')
print()
for i in num[2]:
    print(f'[{i}]', end='')
print()'''

matriz = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
