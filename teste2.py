def fibonacci(x: int):
    numAnterior = 0
    proxNum = 1
    soma = 1
    while soma < x:
        soma = numAnterior + proxNum
        numAnterior = proxNum
        proxNum = soma
    if soma == x: 
        return "Seu número faz parte da sequência de Fibonacci"
    else:
        return "Seu número não pertence a sequência de Fibonacci"

print("-" * 70)    
print(fibonacci(34)) #Numero que faz parte da sequência
print(fibonacci(10)) #Numero que não faz parte da sequência
print("-" * 70)