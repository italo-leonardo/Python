ano = 0
mese = 0
dias = 0
def idade_dias(soma):
    ano_atual = 2024 - ano
    ano_dia = ano_atual * 356
    mese_dia = mese * 30
    soma = ano_dia + mese_dia + dias
    return soma

int(input("Digite seu ano de nascimento: "))
int(input("Digite seu mes de nascimento: "))
int(input("Digite seu dia de nascimento: "))