from sympy import symbols, Piecewise, solve

valor = float(input())
# Parâmetros fornecidos
preco_final = valor  # Preço final
aliquota_icms = 0.12  # Alíquota de ICMS (22%)
aliquota_icmsst = 0.20  # Alíquota de ICMS-ST (22%)
aliquota_ipi = 0.0195  # Alíquota de IPI (1,95%)

# Variável simbólica para o preço de mercado
preco_merc = symbols('preco_merc', positive=True)
preco_pauta = (preco_merc + (preco_merc * aliquota_ipi) ) * 2.4  # Preço da pauta fiscal

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

# Exibir o resultado
print(f"Preço de mercado (precoMerc): {preco_merc_solucoes[0].evalf():.2f}")
