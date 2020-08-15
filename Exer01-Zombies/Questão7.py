#7) Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32

temperatura_celsius = int(input("Digite a temperatura em Celsius: "))
temperatura_fahrenheit = ((9 * temperatura_celsius) / 5) + 32

print(f'A temperatura em Fahrenheit é {temperatura_fahrenheit}')