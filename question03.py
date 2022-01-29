#Código fonte questão 03
#Faturamento

import json  

arquivojson = None
with open("dados.json", "r") as arq_json:
    arquivojson = json.load(arq_json)


def lista_valores(json):  
    lista = []
    soma = 0
    for i in json:
        if json[soma]["valor"] != 0:
            lista.append(json[soma]["valor"])
            soma += 1
        else:
            soma += 1
    return lista


def dias_acima_media():  
    lista = lista_valores(arquivojson)
    media = sum(lista) / len(lista)
    soma1 = 0
    for i in lista:
        if lista[soma1] > media:
            soma1 += 1
        else:
            soma1 += 1
    return soma1


menorfatu = min(lista_valores(arquivojson))
dia_menor = None
soma = 0
for i in arquivojson:
    if arquivojson[soma]["valor"] == min(lista_valores(arquivojson)):
        dia_menor = arquivojson[soma]["dia"]
    soma += 1
maiorfatu = max(lista_valores(arquivojson))
dia_maior = None
soma = 0
for i in arquivojson:
    if arquivojson[soma]["valor"] == max(lista_valores(arquivojson)):
        dia_menor = arquivojson[soma]["dia"]
    soma += 1
diasmedia = dias_acima_media()


print("----------- Programa para calculo de faturamento ------------")
entrada = int(input(print(
    'O que deseja?: (1 - MENOR FATURAMENTO/2 - MAIOR FATURAMENTO/3 - Nº DIAS FATURAMENTO ACIMA DA MÉDIA/4 - SAIR)')))
while entrada == 1 or 2 or 3:
    if entrada == 1:
        print(
            f'Menor faturamento no dia: {dia_menor} no valor de: R$ {menorfatu:.2f}')
        entrada = int(input(print(
            'O que deseja?: (1 - MENOR FATURAMENTO/2 - MAIOR FATURAMENTO/3 - Nº DIAS FATURAMENTO ACIMA DA MÉDIA/4 - SAIR)')))
    elif entrada == 2:
        print(
            f'Maior faturamento no dia: {dia_maior} no valor de: R$ {menorfatu:.2f}')
        entrada = int(input(print(
            'O que deseja?: (1 - MENOR FATURAMENTO/2 - MAIOR FATURAMENTO/3 - Nº DIAS FATURAMENTO ACIMA DA MÉDIA/4 - SAIR)')))
    elif entrada == 3:
        print(
            f'Número de dias com faturamento acima da média mensal: {diasmedia}')
        entrada = int(input(print(
            'O que deseja?: (1 - MENOR FATURAMENTO/2 - MAIOR FATURAMENTO/3 - Nº DIAS FATURAMENTO ACIMA DA MÉDIA/4 - SAIR)')))
    else:
        break