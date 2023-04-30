# Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distancia = float(input("Digite a distancia em km: "))
velocidade_média = float(input("Digite a velocidade média em km/h: "))
tempo = distancia / velocidade_média

print(f"O tempo estimado é de {tempo} horas")