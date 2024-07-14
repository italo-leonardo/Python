idade = 0
def voto():
    ano = int(input('Em que ano você nasceu? '))
    idada = 2024 - ano
    if idade >= 18:
        return print(f'Com {idada} anos: VOTO OBRIGATÒRIO.')
    else:
        return print(f'Com {idada} anos: NÂO VOTA')
voto()