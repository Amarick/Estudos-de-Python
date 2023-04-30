# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salario = float(input("Digite o valor do salario: "))
porce_aumento = float(input("Digite a porcentagem do aumento : "))
aumento = salario * porce_aumento / 100
novo_salario = salario + aumento

print(f"O salario de R$ {salario} recebera um aumento de {porce_aumento} ")
print(f"Com um aumento de R${aumento}. O novo salario será de R${novo_salario}")