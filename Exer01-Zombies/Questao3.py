#3) Escreva um programa que leia a quantidade de dias, horas, minutos e segundos
#do usuário. Calcule o total em segundos.

dia = int(input('Dia: '))
hora = int(input('Horas: '))
minuto = int(input('Minutos: '))
segundo = int(input('Segundos: '))
print(f"O total em segundos é {((dia * 86400) + (hora * 3600) + (minuto * 60) + segundo)}")
