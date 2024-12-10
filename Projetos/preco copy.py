from sympy import symbols, Piecewise, solve

def calcular_preco_mercado(preco_final, aliquota_icms, aliquota_icmsst, aliquota_ipi, fator_pauta):
    """
    Calcula o preço de mercado (precoMerc) dado o preço final, alíquotas de impostos e fator da pauta.
    """
    # Variável simbólica para o preço de mercado
    preco_merc = symbols('preco_merc', positive=True)
    
    # Calcular a pauta fiscal
    preco_pauta = (preco_merc + (preco_merc * aliquota_ipi)) * fator_pauta

    # Cálculo do ICMS
    vlr_icms = preco_merc * aliquota_icms

    # Cálculo do ICMS-ST com base na regra fornecida
    vlr_st = Piecewise(
        ((preco_merc * aliquota_icmsst) - vlr_icms, preco_merc > preco_pauta),
        ((preco_pauta * aliquota_icmsst) - vlr_icms, True)
    )

    # Cálculo do IPI
    vlr_ipi = preco_merc * aliquota_ipi

    # Fórmula do preço final
    preco_final_calculado = preco_merc + vlr_st + vlr_ipi

    # Resolver a equação para encontrar o preço de mercado
    preco_merc_solucoes = solve(preco_final_calculado - preco_final, preco_merc)
    return preco_merc_solucoes[0].evalf()

# Entrada de dados do usuário
try:
    valor = float(input("Digite o preço final desejado (R$): "))
    if valor <= 0:
        raise ValueError("O preço final deve ser um valor positivo.")
except ValueError as e:
    print(f"Erro: {e}")
else:
    # Parâmetros fornecidos
    aliquota_icms = 0.12  # Alíquota de ICMS (12%)
    aliquota_icmsst = 0.20  # Alíquota de ICMS-ST (20%)
    aliquota_ipi = 0.0195  # Alíquota de IPI (1,95%)
    fator_pauta = 2.4  # Fator para cálculo da pauta fiscal

    # Calcular o preço de mercado
    preco_mercado = calcular_preco_mercado(valor, aliquota_icms, aliquota_icmsst, aliquota_ipi, fator_pauta)

    # Exibir o resultado
    print(f"O preço de mercado (precoMerc) necessário é: R$ {preco_mercado:.2f}")
