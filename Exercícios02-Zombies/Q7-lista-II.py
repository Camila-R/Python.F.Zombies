# 7. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
# ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
# em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
# compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.

tamanho_metros = int(input("Metros quadrados da área a ser pintada: "))

# 1l para 3m e 18l para Xm = 3*18 = 54m

if tamanho_metros % 54 == 0:
    latas = tamanho_metros / 54
else:
    latas = int(tamanho_metros / 54) + 1

preco = latas * 80
print(f"A quantidada de latas é {latas}\nE o valor total a ser pago é {preco:.2f}")


