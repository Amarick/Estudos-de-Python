# coleçoes (listas)
preco_1 = 20
preco_2 = 50
preco_3 = 200
# lista
preco =[20,50,200]
#        0, 1, 2
print(preco[0])
print(preco.index(200))
# mostra o indice do valor

# diversidade

diversidade = [15,'victor', True]
print(diversidade[0])
print(diversidade[1])
print(diversidade[2])


# laços
for preco in preco:
    print(preco)



idade = [15,46,75,34,23]
total = 0
for idade in idade:
    total = total + idade
    print(total)
