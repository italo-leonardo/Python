media = 0
soma = 0
velho = 0
nomeVelho = ''
menos20 = 0
for c in range(1, 5):
    print(f'------ {c}º Pessoa ------')
    nome = input('Digite seu nome: ')
    idade = int(input('Digite seu idade: '))
    sexo = int(input('Digite 1 homen e 2 Mulher: '))
    print('\n')
    media += idade
    soma = media / 4
    if sexo == 1:
        if idade > velho:
            velho = idade
            nomeVelho = nome
    if sexo == 2:
        if idade < 20:
            menos20 +=1 
        
print('A media da Idade do Grupo é de {} Anos.'.format(soma))
print('O nome do Humem mais velho é {} com {} Anos.'.format(nomeVelho,velho))
print('{} Mulheres tem manos de 20 anos.'.format(menos20))