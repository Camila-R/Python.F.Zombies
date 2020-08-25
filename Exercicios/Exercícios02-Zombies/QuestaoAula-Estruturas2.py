# Modifique o programa da empresa Tchau para uma promoção onde a tarifa é de R$ 0.08 quando você utiliza mais
# que 800min

##deu errado!!


tempo_ligacao = int(input("Quantos minutos de ligação no mês: "))

if tempo_ligacao < 200:
    preco = 0.2
elif tempo_ligacao <= 400:
    preco = 0.18
elif tempo_ligacao <= 800:
    preco = 0.15
else:
    preco = 0.08

print(f"O valor da sua conta de telefone é R${tempo_ligacao * preco:.2f} reais")