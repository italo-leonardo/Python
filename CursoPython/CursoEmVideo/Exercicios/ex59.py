'''cont = 1
escolha = 0
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

while cont > 0:
    print('[1]somar\n[2]multiplicar\n[3]maior\n[4]novos número\n[5]sair do programa.')
    escolha = int(input("Digite uma opção: "))
    if escolha == 1:
        soma = n1 + n2
        print(f"A soma de {n1} + {n2} = {soma}")
    if escolha == 2:
        mult = n1 * n2
        print(f"A multiplicação de {n1} + {n2} = {mult}")
    if escolha == 3:
        if n1 > n2:
            print(f'O maior valor é {n1}')
        else:
            print(f"O maior valor é {n2}")
    if escolha == 4:
        n1 = int(input("Digite o primeiro numero: "))
        n2 = int(input("Digite o segundo numero: "))
    if escolha == 5:
        print("FIM DO PROGRAMA!")
        cont -= 1'''
from time import sleep
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
opção = 0
while opção != 5:
    print('[1]somar\n[2]multiplicar\n[3]maior\n[4]novos número\n[5]sair do programa.')
    opção = int(input("Digite uma opção: "))
    if opção == 1:
        soma = n1 + n2
        print(f"A soma de {n1} + {n2} = {soma}")
    elif opção == 2:
        mult = n1 * n2
        print(f"A multiplicação de {n1} + {n2} = {mult}")
    elif opção == 3:
        if n1 > n2:
            print(f'O maior valor é {n1}')
        else:
            print(f"O maior valor é {n2}")
    elif opção == 4:
        n1 = int(input("Digite o primeiro numero: "))
        n2 = int(input("Digite o segundo numero: "))
    elif opção == 5:
        print("FIM DO PROGRAMA!")
    else: 
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    sleep(0.5)
print("Fim do programa! Volte sempre!")