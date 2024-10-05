def somarIndice(indice: int): #Decidi fazer uma função para o script aceitar outros indices

    k = 0
    soma = 0

    while k < indice:
        k = k + 1
        soma = soma + k
    return soma

print("-" * 70)
print(somarIndice(13)) #Retornará 91 para o indice 13
print("-" * 70)