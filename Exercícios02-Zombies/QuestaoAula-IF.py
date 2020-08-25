#Pergunte a velocidade de um carro, supondo um valor inteiro. Caso ultrapasse 110km/h, exiba uma mensagem dizendo que
# o usuário foi multado. Neste caso, exiba o valor da multa, cobrando R$ 5,00 por km acima de 110.

velocidade = int(input("Velocidade ultrapassada: "))

if velocidade > 110:
    print("Você foi multado! Ultrapassou o limite de velocidade")
    valor_multa = (velocidade - 110) * 5
    print(f"O valor da multa é R${valor_multa:.2f} reais")