#4. Faça um Programa que leia três números e mostre o maior deles.

number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
number3 = int(input("Digite o terceiro número: "))

if number1 > number2 and number1 > number3:
    print(f"O maior número é {number1}")
elif number2 > number1 and number2 > number3:
    print(f"O maior número é {number2}")
else:
    print(f"O maior número é {number3}")

# ou   max(number1, number2, number3)
#     print(f"O maior valor é {max}")