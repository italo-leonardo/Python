print("jj")
cont100 = 0
valor = int(input())
total = valor

while total > 0:
    if total >= 100:
        total -= 100
        cont100 +=1 
print(cont100, valor, total)
