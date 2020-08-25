# 1. Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser
# um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

lado_a = int(input("Indique o primeiro lado do triângulo: "))
lado_b = int(input("Indique o segundo lado do triângulo: "))
lado_c = int(input("Indique o terceiro lado do triângulo: "))

if lado_a + lado_b > lado_c:
    print("É um triângulo!")
    if lado_a == lado_b == lado_c:
        print("Este é um Triângulo Equilátero, porque possui os 03 lados iguais")
    else:
        if lado_a == lado_b != lado_c or lado_a != lado_b == lado_c or lado_a == lado_c != lado_b:
            print("Este é um Triângulo Isósceles, porque possui os 02 lados iguais e 01 lado diferente")
        else:
            print("Este é um Triângulo Escaleno, porque todos os lados são diferentes")

else:
    print("Não é um triângulo")
