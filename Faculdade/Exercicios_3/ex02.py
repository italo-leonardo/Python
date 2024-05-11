def soma_digitos(numero):
    soma = 0
    while numero > 0:
        digito = numero % 10
        soma += digito
        numero //= 10
    return soma 
numero = int(input("Digite seu numero: "))
print("A soma dos digitos de", numero, "é", soma_digitos(numero))