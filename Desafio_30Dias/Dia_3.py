def calcula_duracao(h_ini, m_ini, h_fim, m_fim):
    ini_min = h_ini * 60 + m_ini
    fim_min = h_fim * 60 + m_fim

    if fim_min > ini_min:
        duracao_min = fim_min - ini_min
    else:
        duracao_min = (24 * 60 - ini_min) + fim_min

    horas = duracao_min // 60
    minutos = duracao_min % 60

    return horas, minutos

h_ini, m_ini, h_fim, m_fim = map(int, input().split())

horas, minutos = calcula_duracao(h_ini, m_ini, h_fim, m_fim)

print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')
