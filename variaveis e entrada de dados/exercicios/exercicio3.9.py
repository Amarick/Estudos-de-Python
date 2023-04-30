# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

# Um minuto tem 60 segundos
# Uma hora tem 3600 (60 * 60) segundos
# Um dia tem 24 horas, logo 24 * 3600 segundos

dias = int(input("Digite a quantidade de dias : "))
horas = int(input("Digite a quantidade de horas : "))
minutos = int(input("Digite a quantidade de minutos : "))
segundos = int(input("Digite a quantidade de segundos : "))

valor_em_segundos = dias * 24 * 3600 + horas * 3600 + minutos * 60 + segundos

print(f"Os valores digitados equivalem em segundos a {valor_em_segundos} segundos.")


