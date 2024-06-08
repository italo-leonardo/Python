valor = float(input())
n100 = n50 = n20 = n10 = n5 = n2 = 0
m1 = m50 = m25 = m10 = m5 = m01 = 0

valor = round(valor * 100)  # Converter o valor para centavos para evitar problemas de precisão

if valor >= 10000:
    n100 = valor // 10000
    valor %= 10000
if valor >= 5000:
    n50 = valor // 5000
    valor %= 5000
if valor >= 2000:
    n20 = valor // 2000
    valor %= 2000
if valor >= 1000:
    n10 = valor // 1000
    valor %= 1000
if valor >= 500:
    n5 = valor // 500
    valor %= 500
if valor >= 200:
    n2 = valor // 200
    valor %= 200
if valor >= 100:
    m1 = valor // 100
    valor %= 100
if valor >= 50:
    m50 = valor // 50
    valor %= 50
if valor >= 25:
    m25 = valor // 25
    valor %= 25
if valor >= 10:
    m10 = valor // 10
    valor %= 10
if valor >= 5:
    m5 = valor // 5
    valor %= 5
if valor >= 1:
    m01 = valor

print('NOTAS:')
print(f'{int(n100)} nota(s) de R$ 100.00')
print(f'{int(n50)} nota(s) de R$ 50.00')
print(f'{int(n20)} nota(s) de R$ 20.00')
print(f'{int(n10)} nota(s) de R$ 10.00')
print(f'{int(n5)} nota(s) de R$ 5.00')
print(f'{int(n2)} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{int(m1)} moeda(s) de R$ 1.00')
print(f'{int(m50)} moeda(s) de R$ 0.50')
print(f'{int(m25)} moeda(s) de R$ 0.25')
print(f'{int(m10)} moeda(s) de R$ 0.10')
print(f'{int(m5)} moeda(s) de R$ 0.05')
print(f'{int(m01)} moeda(s) de R$ 0.01')
