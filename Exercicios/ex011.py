n1 = int(input("Digite um numero: "))
n2 = int(input("Digite segundo numero: "))
n3 = int(input("Digite terceiro numero: "))

if n1 > n2 and n1 > n3 and n2 > n3:
    print("Sequancia de Descrescente:", n1, n2, n3)
if n2 > n1 and n2 > n3 and n1 > n3:
    print("Sequancia de Descrescente:", n2, n1, n3)
if n3 > n1 and n3 > n2 and n1 > n2:
    print("Sequancia de Descrescente:", n3, n1, n2)
if n3 > n1 and n3 > n2 and n1 < n2:
    print("Sequancia de Descrescente:", n3, n2, n1)
else: 
    print("Comando inválido")