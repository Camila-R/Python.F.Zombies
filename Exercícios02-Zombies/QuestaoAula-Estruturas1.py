# Considere a empresa de telefonia Tchau. Abaixo de 200min, a empresa cobra R$0,20 por min.
# Entre 200 e 400 min, o preço é R$ 0,18 por min. Acima de 400min é de R$ 0,15 por min.
# Calcule a conta de telefone.

tempo_ligacao = int(input("Quantos minutos de ligação no mês: "))

if tempo_ligacao <= 200:
    preco = 0.2
else:
    if tempo_ligacao <= 400:
        preco = 0.18
    else:
        preco = 0.15

conta_telefone = tempo_ligacao * preco
print(f"O valor da sua conta de telefone é R${conta_telefone:.2f} reais")