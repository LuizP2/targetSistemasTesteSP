def fibonacci(x: int):
    numAnterior = 0
    numAtual = 1
    soma = 1
    while soma < x:
        soma = numAnterior + numAtual # Soma o numero anterior ao atual
        numAnterior = numAtual # Atualiza o valor do numero anterior
        numAtual = soma # Atualiza o valor do numero atual
    if soma == x: 
        return "Seu número faz parte da sequência de Fibonacci"
    else:
        return "Seu número não pertence a sequência de Fibonacci"

print("-" * 70)    
print(fibonacci(34)) #Numero que faz parte da sequência
print(fibonacci(10)) #Numero que não faz parte da sequência
print("-" * 70)