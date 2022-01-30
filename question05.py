#Código fonte questão 05
#String invertida

def palavra_invertida(palavra): 
    if len(palavra) == 0: 
        return palavra 
    else: 
        return palavra_invertida(palavra[1:]) + palavra[0] 
  
palavra = input(print("Digite uma palavra: "))
  
print("A palavra original é: ",end="") 
print(palavra) 
  
print("A palavra invertida é: ",end="") 
print(palavra_invertida(palavra))
