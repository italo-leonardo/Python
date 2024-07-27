'''def lin():
    print("-"*30)

lin()
print("CURSO EM VIDEO")
lin()'''

'''def titulo(txt):
    print("-"*30)
    print(f'{txt:>20}')
    print("-"*30)

titulo("Ola munda")'''

'''def soma(a, b):
    print(f"A = {a} e B = {b}")
    s = a + b
    print(f"A soma A + B = {s}")

soma(5, 5)'''

'''def contador(*num): # * simbolo para quando não sabe quantos valores vai recebe.
    soma = 0
    for i in num:
        soma += i
    print(soma)

contador(2,1,7)
contador(8,0)
contador(4,4,7,6,2)'''

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(lst)

valores = [6,3,9,1,0,2]
print(valores)
dobra(valores)
