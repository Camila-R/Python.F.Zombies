#6) Calcule o tempo de uma viagem de carro.
#Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distancia = int(input("Insira a distância a percorrer em Km: "))
velocidade_media = int(input("Insira a velocidade média esperada em Km/h: "))

tempo_viagem = (distancia / velocidade_media)

print(f"O tempo total de viagem de carro é de {tempo_viagem} horas")