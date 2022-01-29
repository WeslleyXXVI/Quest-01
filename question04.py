#Código fonte questão 04
#Porcentagem de representatividade por estado

class Cadastrar:
    def __init__(self, estado, valor):
        self.estado = estado
        self.valor = valor


def porc_total(total, obj):
    mensal = total
    valor = obj
    return (valor / mensal) * 100


fatu1 = Cadastrar("SP", float(67836.43))
fatu2 = Cadastrar("RJ", float(36678.66))
fatu3 = Cadastrar("MG", float(29229.88))
fatu4 = Cadastrar("ES", float(27165.48))
fatu5 = Cadastrar("Outros", float(19849.53))
lista = [fatu1, fatu2, fatu3, fatu4, fatu5]
fatutotal = 0
soma = 0
for i in lista:
    fatutotal += float(lista[soma].valor)
cont = 0
soma1 = 0
while cont < len(lista):
    for i in lista:
        print('------------------------------------')
        print(f'Faturamento total: R${fatutotal:.2f}')
        print('Estado: ', lista[soma1].estado)
        print('Faturamento: R$', lista[soma1].valor)
        print(
            f'% do faturamento total: {porc_total(fatutotal, lista[soma1].valor):.2f}%')
        soma1 += 1
        cont += 1