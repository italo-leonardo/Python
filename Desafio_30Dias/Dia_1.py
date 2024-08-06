# beecrowd | 1051
 
salario = float(input("Digite seu salario: "))

if salario <= 2000.00:
    print('Isento')
else:
    imposto = 0.0
    faixas = [
        (2000.00, 0.00), (1000.00, 0.08), (1500.00, 0.18), (float('inf'), 0.28) 
    ]

    resto = salario
    for i in range(len(faixas)-1):
        faixa, aliquota = faixas[i]
        if resto > faixa:
            imposto += faixa * aliquota
            resto -= faixa
        else:
            imposto += resto * aliquota
            resto = 0
            break
    
    if resto > 0:
        imposto += resto * 0.28

    print(f'R$ {imposto:.2f}')







