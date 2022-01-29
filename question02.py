#Código fonte questão 02
#Sequencia de Fibonacci

numero = int(input("Digite um numero: "))
primeiro = 0
segundo = 1
soma = 0
i = 0
lista = []
lista.append(primeiro)
lista.append(segundo)
while soma < 10000:
    soma = int(lista[i]) + int(lista[i+1])
    primeiro = int(lista[i+1])
    segundo = soma
    lista.append(segundo)
    i += 1
if numero in lista:
    print(f"O número {numero} pertece à sequencia de Fibonacci")
else:
    print(f"O número {numero} não pertece à sequencia de Fibonacci")