"Erro"
n = int(input("Digite um número: "))
fato = 0
salva = n
guarda = 0
while n > 1:
    menos = n - 1
    mult = salva * menos
    guarda += mult
    print(guarda)
    fato = guarda * menos
    n -= 1    
print(fato)


