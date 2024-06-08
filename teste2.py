valor = float(input())
n100 = n50 = n20 = n10 = n5 = n2 = 0
m1 = m50 = m25 = m10 = m5 = m01 = 0

if valor >= 100:
    n100 = valor // 100
    valor%=100 
if valor >= 50:
    n50 = valor // 50
    valor %= 50
if valor >= 20:
    n20 = valor // 20
    valor %= 20
if valor >= 10:
    n10 = valor // 10
    valor %= 10
if valor >= 5:
    n5 = valor // 5
    valor %= 5
if valor >= 2:
    n2 = valor // 2
    valor %= 2
if valor >= 1:
    m1 = valor // 1.00
    valor %= 1
if valor >= 0.50:
    m50 = valor // 0.50
    valor %= 0.50
if valor >= 0.25:
    m25 = valor // 0.25
    valor %= 0.25
if valor >= 0.10:
    m10 = valor // 0.10
    valor %= 0.10
if valor >= 0.05:
    m5 = valor // 0.05
    valor %= 0.05
else:
    m01 = valor // 0.01
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