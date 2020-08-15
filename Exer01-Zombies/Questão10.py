#10) Escreva um programa para calcular a redução do tempo de vida de um fumante.
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
# Considere que um fumante perde 10 minutos de vida a cada cigarro.
# Calcule quantos dias de vida um fumante perderá. Exiba o total de dias.

cigarros_dia = int(input("Quantos cigarros você fuma por dia? Digite: "))
fumante_anos = int(input("Quantos anos você fumou? Digite: "))

cigarro_vida = (cigarros_dia * (10 / 1440))
anos_vida = (fumante_anos * 365)
vida_perda = (anos_vida * cigarro_vida)

print(f'Você perdeu {vida_perda} dias')