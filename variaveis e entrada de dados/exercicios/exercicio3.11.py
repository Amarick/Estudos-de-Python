# Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

mercadoria = float(input("Digite o valor da mercadoria R$ "))
perce_desconto = float(input("Digite o percentual do desconto "))

valor_desconto = mercadoria * perce_desconto / 100

pagamento = mercadoria - valor_desconto

print(f"O valor da mercadoria é de R$ {mercadoria}.")
print(f"valor do desconto {valor_desconto} %")
print(f"valor à pagar: R$ {pagamento}")