
fatDiario = {1: 22174.1664, # Dicionário de valores referentes a cada dia
             2: 24537.6698,
             3: 26139.6134,
             6: 26742.6612,
             8: 42889.2258,
             9: 46251.174,
             10: 11191.4722,
             13: 3847.4823,
             14: 373.7838,
             15: 2659.7563,
             16: 48924.2448,
             17: 18419.2614,
             20: 35240.1826,
             21: 43829.1667,
             22: 18235.6852,
             23: 4355.0662,
             24: 13327.1025,
             27: 25681.8318,
             28: 1718.1221,
             29: 13220.495,
             30: 8414.61}

def menorfaturamento(dias):
    res = dias[1] # Atribui o valor do primeiro item do dicionário ao res
    for dia, faturamento in dias.items():
        if faturamento < res: # Checa se o valor do faturamento é menor que o anterior
            res = faturamento # Caso verdadeiro, substitui o valor de res pelo menor
    return res

def maiorfaturamento(dias):  
    res = dias[1]
    for dia, faturamento in dias.items():
        if faturamento > res: # Igual a função anterior, porém checa se o valor é maior
            res = faturamento
    return res

def mediafaturamento(dias):
    fatTotal = 0
    res = dias[1]
    for media, faturamento in dias.items():
        fatTotal = fatTotal + faturamento # Soma os faturamentos ao faturamento total
        res = fatTotal / len(fatDiario) # Divide o faturamento pela quantidade de dias para tirar a média
    return res

print("-" * 70)
print(f"O menor faturamento é: {menorfaturamento(fatDiario):.2f}") # Usei :.2f para formatar o numero em 2 casas decimais. Caso queiram o resultado completo, basta tirar estes caracteres do comando print.
print(f"O maior faturamento é: {maiorfaturamento(fatDiario):.2f}")
print(f"A média de faturamento é: {mediafaturamento(fatDiario):.2f}")
print("-" * 70)