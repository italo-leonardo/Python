def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATÒRIO.'
    else:
        return f'Com {idade} anos: NÂO VOTA'
    
print(voto(int(input('Em que ano vc nasceu? '))))

