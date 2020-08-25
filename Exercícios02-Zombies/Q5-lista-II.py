#5. Faça um Programa que leia três números e mostre o maior e o menor deles.

number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
number3 = int(input("Digite o terceiro número: "))

#Opção1
maior_numero = max(number1, number2, number3)
menor_numero = min(number1, number2, number3)
print(f"O maior valor é {maior_numero} e o menor é {menor_numero}")



#Opção2
#if number1 > number2 and number1 > number3 and number2 < number3:
#    print(f"O maior número é {number1} e o menor número é {number2}")
#elif number2 > number1 and number2 > number3 and number3 < number1:
#    print(f"O maior número é {number2} e o menor número é {number3}")
#else:
#    print(f"O maior número é {number3} e o menor número é {number1}")



#Opção03
# maior_numero, menor_numero = max(number1, number2, number3), min(number1, number2, number3)
# print(f"O maior valor é {maior_numero} e o menor é {menor_numero}")