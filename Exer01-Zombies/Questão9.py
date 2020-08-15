#9) Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
#usuário, assim como a quantidade de dias pelos quais o carro foi alugado.
# Calcule o preço a pagar, sabendo que:

# carro custa R$ 60,00 por dia
# R$ 0,15 por km rodado.

km_percorridos = int(input("Digite a quantidade de KM a serem percorridos: "))
dias_aluguel = int(input("Digite os dias alugados: "))

custo_carro_km = (km_percorridos * 0.15)
custo_carro_dia = (dias_aluguel * 60)
total_pagar = (custo_carro_km + custo_carro_dia)

print(f'O total a pagar pelo carro alugado é {total_pagar}')