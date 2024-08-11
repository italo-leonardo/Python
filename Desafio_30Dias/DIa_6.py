mes = ['','January', 'February', 'March', 
       'April','May', 'June', 'July',
       'August', 'September', 'October',
       'November', 'December']

while True:
    num = int(input('Digite o numero do mes: '))
    if num <=0 or num > 12:
        print('Valor nao esta dentro do padrão solicitado')
    else:
        print(mes[num])
        break