fatMensal = {"SP": 67836.43, #Dicionário para atribuir os valores de cada estado
             "RJ": 36678.66,
             "MG": 29229.88,
             "ES": 27165.48,
             "outros": 19849.53}

def percentual(Estado):
    fatTotal = 0
    res = 0
    for estado, faturamento in fatMensal.items():
        fatTotal = fatTotal + faturamento # Soma os faturamentos ao faturamento total
    res = (Estado) / fatTotal * 100 # Calcula a porcentagem
    return res

print("-" * 70)
print(f"o faturamento de São Paulo foi de {percentual(fatMensal["SP"]):.2f}%")
print(f"o faturamento do Rio de Janeiro foi de {percentual(fatMensal["RJ"]):.2f}%")
print(f"o faturamento de Mato Grosso foi de {percentual(fatMensal["MG"]):.2f}%")
print(f"o faturamento de Espírito Santo foi de {percentual(fatMensal["ES"]):.2f}%")
print(f"o faturamento dos outros estados foi de {percentual(fatMensal["outros"]):.2f}%") # Usei :.2f para formatar o numero em 2 casas decimais. Caso queiram o resultado completo, basta tirar estes caracteres do comando print.
print("-" * 70)