#8) Faça agora o contrário da questão 7, de Fahrenheit para Celsius. ((32 °F − 32) × 5/9 = 0 °C)

temperatura_fahrenheit = int(input("Digite a temperatura em Fahrenheit: "))
temperatura_celsius = ((temperatura_fahrenheit - 32) * 5) / 9

print(f'A temperatura em Celsius é {temperatura_celsius}')