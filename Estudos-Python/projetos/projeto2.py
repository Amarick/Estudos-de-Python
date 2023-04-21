#  chute um numero
# escreva um programa que, ao iniciar gera im valor aleatório de 1 a 10 epermite que o usuário chute um número até que o valor aleatório gerado no início do programa seja chutado corretamente! 
# O programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado no início do programa

import random
valor_aleatorio = random.randint(1,10)
acertou = False
while acertou == False:
    chute = int(input ("Chute um valor de 1 a 10 "))
    if chute > valor_aleatorio:
        print("Seu chute foi maior que o valor gerado ")

    elif chute < valor_aleatorio:
        print("Seu chute foi menor que o valor gerado ")

    elif chute == valor_aleatorio:
        acertou = True
        print("Você acertou! ")    


