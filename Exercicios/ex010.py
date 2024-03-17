l1 = int(input("Digite o primeiro lado: "))
l2 = int(input("Dgite o segundo lado: "))
l3 = int(input("Digite o terceiro lado: "))

if l1 == l2 and l1 == l3 and l2 == l3:
    print("Triangulo Equilátero")
if l1 != l2 and l1 != l3 and l2 != l3:
    print("Triangulo escaleno")
if l1 == l2 or l1 or l3 or l2 != l3:
    print("Triangulo isosceles")