# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS,
# quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os
# descontos e o salário líquido, conforme a tabela abaixo:
# a. + Salário Bruto : R$
# b. - IR (11%) : R$
# c. - INSS (8%) : R$
# d. - Sindicato ( 5%) : R$
# e. = Salário Liquido : R$

salario_hora = float(input("Quanto você ganha por hora? "))
mes_calculo = str(input("Qual o mês de referência? "))
hora_trabalhada = int(input(f"Quantas horas trabalhadas para {mes_calculo}?: "))

salario_bruto = salario_hora * hora_trabalhada
desconto_ir = (salario_bruto * 11) / 100
desconto_inss = (salario_bruto * 8) / 100
desconto_sindicato = (salario_bruto * 5) / 100
salario_liquido = salario_bruto - (desconto_ir + desconto_inss + desconto_sindicato)

print(f"a. Salário Bruto: R${salario_bruto} reais\nb. Desconto do Imposto de Renda (11%): R${desconto_ir:.2f} reais")
print(f"c. Desconto do INSS (8%): R${desconto_inss:.2f} reais\nd. Desconto do Sindicado (5%): R${desconto_sindicato:.2f} reais")
print(f"e. Salário líquido para o mês de {mes_calculo}: R${salario_liquido:.2f} reais")


