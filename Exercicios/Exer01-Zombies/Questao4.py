#4) Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
#porcentagem do aumento. Exiba o valor do aumento e do novo salário.

valor_salario = int(input("Insira o valor do salário: "))
porcentagem_aumento = int(input("Insira a porcentagem do aumento: "))

valor_aumento = (porcentagem_aumento * valor_salario)/100
novo_salario = valor_salario + ((porcentagem_aumento * valor_salario)/100)

print(f"O total do aumento é {valor_aumento} e o novo salário é {novo_salario}")