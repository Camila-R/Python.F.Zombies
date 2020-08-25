#5) Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

preco = int(input("Insira o preço: "))
desconto = int(input("Insira a porcentagem do desconto: "))

total_desconto = (desconto * preco)/100
novo_preço = preco - ((desconto * preco)/100)

print(f"O total do desconto é {total_desconto} e o preço a pagar é {novo_preço}")