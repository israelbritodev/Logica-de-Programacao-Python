'''
Escreva um programa para ler um ÚNICO caractere e depois 
informar se este é uma vogal, um número ou uma operação matemática (+, -, * ou /). 
'''

caractere = input()

if caractere.isnumeric():
  print("O caractere é um número")
elif caractere in "+-*/":
  print("O caractere é uma operação matemática")
elif caractere.lower() in "aeiou":
  print("O caractere é uma vogal")
  
'''
  Faça um programa para ler dois número (n1 e n2) e uma operação da matemática
  (+, -, * ou /) e exiba o resultado dessa operação entre esses dois números.
'''

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, * ou /): ")

if operacao == "+":
    resultado = n1 + n2
    print(f"Você escolheu a operação de soma. O resultado dessa operação é {resultado:.2f}")
elif operacao == "-":
    resultado = n1 - n2
    print(f"Você escolheu a operação de subtração. O resultado dessa operação é {resultado:.2f}")
elif operacao == "*":
    resultado = n1 * n2
    print(f"Você escolheu a operação de multiplicação. O resultado dessa operação é {resultado:.2f}") 
elif operacao == "/":
    if n2 != 0:
        resultado = n1 / n2
        print(f"Você escolheu a operação de divisão. O resultado dessa operação é {resultado:.2f}")
    else:
        resultado = "Erro: Divisão por zero não é permitida."
else:
    resultado = "Operação inválida."
    
'''
Faça um programa que leia o nome, o sobrenome e a idade de um atleta e exiba seu nome completo e se ele está na 
categoria infantil (menor de 12 anos), juvenil (entre 12 e 17 anos), adulto (entre 18 e 35 anos) ou master (acima de 35 anos).
'''

nome = str(input("Digite o nome do atleta: "))
sobrenome = str(input("Digite o sobrenome do atleta: "))
idade = int(input("Digite a idade do atleta: "))

nome_completo = nome + " " + sobrenome

if idade < 12:
    print(f"A categoria do atleta {nome_completo} é a infantil.")
elif idade < 18:
    print(f"A categoria do atleta {nome_completo} é a juvenil.")
elif idade < 36:
    print(f"A categoria do atleta {nome_completo} é a adulto.")
else:
    print(f"A categoria do atleta {nome_completo} é a master.")
    
'''
Faça um programa que leia o valor da diária de um funcionário, a quantidade de dias que este trabalhou no mês e 
exiba o salário bruto, o Imposto de Renda (IR) a ser pago e o salário líquido. 
O cálculo do IR deve considerar os seguintes percentuais:

Salário até R$2.000,00 é isento de IR

Salário entre R$2.000,00 e R$5.000,00 deve pagar 15% de IR

Salário superior a R$5.000,00 deve pagar 27,5% de IR.

'''

valor_diaria = float(input("Digite o valor da diária do funcionário: R$"))
dias_trabalhados = int(input("Digite a quantidade de dias trabalhados no mês: "))

salario_bruto = valor_diaria * dias_trabalhados

if salario_bruto <= 2000:
    ir = 0
elif salario_bruto <= 5000:
    ir = salario_bruto * 0.15
else:
    ir = salario_bruto * 0.275

salario_liquido = salario_bruto - ir

if ir == 0:
  print("Você está isento do Imposto de Renda.")
  print(f"Seu salário é: R$ {salario_bruto:.2f}")
else:
  print("Você não está isento do Imposto de Renda.")
  print(f"Seu salário bruto é de: R$ {salario_bruto:.2f}")
  print(f"Seu valor do IR é: R$ {ir:.2f}")
  print(f"Seu salário líquido é de: R$ {salario_liquido:.2f}")
  
  
'''
  Faça um programa para ler a média salarial dos funcionários e, na sequência, o nome e o salário de um dos 
  funcionários dessa empresa. Ao terminar a leitura, exibir o nome do funcionário e se o seu salário é maior, 
  menor ou igual a média salarial.
'''

media_salarial = float(input("Digite a média salarial dos funcionários: R$"))
nome_funcionario = str(input("Digite o nome do funcionário: ")) 
salario_funcionario = float(input("Digite o salário do funcionário: R$"))

resultado = salario_funcionario - media_salarial

if salario_funcionario > media_salarial:
    print(f"{nome_funcionario} recebe R$ {resultado:.2f} a mais do que a média salarial da empresa.")
elif salario_funcionario < media_salarial:
    print(f"{nome_funcionario} recebe R$ {resultado:.2f} a menos do que a média salarial da empresa.")
else:
    print(f"{nome_funcionario} recebe igual a média salarial da empresa.")

'''
Escreva um programa para ler o tamanho de três segmentos de retas e informar se estas podem formar um triângulo (a soma de quaisquer dois lados sempre deve ser maior que o terceiro lado).

Caso sim, também deve-se informar se este é equilátero (tem os três lados iguais), escaleno (tem os três lados diferentes) ou isósceles (tem apenas dois lados iguais).
'''

lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("Os segmentos podem formar um triângulo.")
    if lado1 == lado2 == lado3:
        print("O triângulo é equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("O triângulo é isósceles.")
    else:
        print("O triângulo é escaleno.")
else:
    print("Os segmentos não podem formar um triângulo.")

'''
Faça um programa para ler quatro números inteiros (n1, n2, n3 e n4) e 
depois exibir todos que são pares e positivos, pares e negativos, ímpares e positivos, ímpares e negativo e zero, nesta ordem
'''

n1 = int(input())
n2 = int(input()) 
n3 = int(input())
n4 = int(input())

print("Números pares e positivos:")

if n1 % 2 == 0 and n1 > 0:
    print(n1)

if n2 % 2 == 0 and n2 > 0:
    print(n2)
if n3 % 2 == 0 and n3 > 0:
    print(n3)
if n4 % 2 == 0 and n4 > 0:
    print(n4)
print()
print("Números pares e negativos:")
if n1 % 2 == 0 and n1 < 0:
    print(n1)
if n2 % 2 == 0 and n2 < 0:
    print(n2)
if n3 % 2 == 0 and n3 < 0:
    print(n3)
if n4 % 2 == 0 and n4 < 0:
    print(n4)
print()
print("Números ímpares e positivos:")
if n1 % 2 != 0 and n1 > 0:
    print(n1)
if n2 % 2 != 0 and n2 > 0:
    print(n2)
if n3 % 2 != 0 and n3 > 0:
    print(n3)
if n4 % 2 != 0 and n4 > 0:
    print(n4)
print()
print("Números ímpares e negativos:")
if n1 % 2 != 0 and n1 < 0:  
    print(n1)
if n2 % 2 != 0 and n2 < 0:
    print(n2)
if n3 % 2 != 0 and n3 < 0:
    print(n3)
if n4 % 2 != 0 and n4 < 0:
    print(n4)

print()
print("Números zeros:")

if n1 == 0:
    print(n1)
if n2 == 0:
    print(n2)
if n3 == 0:
    print(n3)
if n4 == 0:
    print(n4)
    
