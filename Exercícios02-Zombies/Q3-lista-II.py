#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
# (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a
# variável peso (peso de peixes) e verifique se há excesso. Se houver, gravar na variável excesso e na variável multa
# o valor da multa que João deverá pagar. Caso contrário mostrar tais variáveis com o conteúdo ZERO.


peso = float(input("Digite o valor do peso (Kg): "))
excedente = peso - 50
multa = excedente * 4

if peso > 50:
    print(f"O peso é {peso}kg\n O excedente é de {excedente}kg\n O valor da multa é R${multa} reais")
else:
    print(f"O peso é {peso}kg\n O excedente é Zero e a multa é Zero")


#ou
#mensagem_multa = f'O peso eh {peso}kg\nO excedente eh {excedente}kg\nA multa eh R${multa} reais'
#mensagem_ok = f'O peso é {peso}kg\nO excedente é ZERO e a multa é ZERO'
#   print(mensagem_multa) if peso > 50 else print(mensagem_ok)