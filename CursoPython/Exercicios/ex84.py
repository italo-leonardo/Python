pessoas = list()
dados = list()
while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    dados.append(nome)
    dados.append(peso)
    pessoas.append(dados[:])
    dados.clear()
    op = str(input('Quer continuar? [S/N]: ')).upper()
    if op != 'S':
        break

print('-='*30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O manior peso foi de {max(pessoas)}Kg.')