# Leitura dos valores de entrada
n = input().split()
n1, n2, n3 = int(n[0]), int(n[1]), int(n[2])

# Determina os valores mínimo, médio e máximo
if n1 < n2:
    if n1 < n3:
        min_val = n1
        if n2 < n3:
            mid_val = n2
            max_val = n3
        else:
            mid_val = n3
            max_val = n2
    else:
        min_val = n3
        mid_val = n1
        max_val = n2
else:
    if n2 < n3:
        min_val = n2
        if n1 < n3:
            mid_val = n1
            max_val = n3
        else:
            mid_val = n3
            max_val = n1
    else:
        min_val = n3
        mid_val = n2
        max_val = n1

# Impressão dos valores ordenados
print(min_val)
print(mid_val)
print(max_val)

# Impressão dos valores na ordem original
print()
print(n1)
print(n2)
print(n3)
