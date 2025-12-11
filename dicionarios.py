# Faça um programa que receberá n pares de dados: uma categoria e um valor inteiro. 
# O seu código deve somar os valores por categoria e imprimir o total de cada uma.
#   Exemplo de entrada:
#   n -> inteiro
#   n linhas, cada uma com uma categoria (string) e um valor (inteiro)

n = int(input("Digite o número de pares categoria-valor: "))
soma_por_categoria = {}
for _ in range(n):
    categoria, valor = input("Digite a categoria e o valor separados por espaço: ").split()
    valor = int(valor)
    if categoria in soma_por_categoria:
        soma_por_categoria[categoria] += valor
    else:
        soma_por_categoria[categoria] = valor

for categoria, total in soma_por_categoria.items():
    print(f"{categoria}: {total}")
    

# Faça um programa que armazena números de telefone de algumas pessoas em um dicionário. 
# O programa deve receber entradas no formato nome telefone, uma por linha, até que o usuário digite "fim" 
# para encerrar o cadastro. Depois disso, o programa deve ler um nome e 
# imprimir o número correspondente, caso exista no dicionário.

agenda = {}
while True:
    entrada = input("Digite nome e telefone separados por espaço (ou 'fim' para encerrar): ")
    if entrada.lower() == "fim":
        break
    nome, telefone = entrada.split()
    nome = nome.lower()
    agenda[nome] = telefone
    
nome_consulta = input("Digite o nome para consulta: ")
if nome_consulta.lower() in agenda:
    print(f"Telefone de {nome_consulta}: {agenda[nome_consulta]}")
else:
    print("Essa pessoa não está na agenda.")

# Faça um programa que receberá nomes de pessoas, um por linha, até que o usuário digite "fim". 
# Ao final, agrupe e imprima os nomes de acordo com a primeira letra do nome, ignorando se está 
# em maiúsculo ou minúsculo. 
# Os nomes devem ser agrupados em ordem alfabética da letra inicial e exibidos na ordem de inserção.
#       A entrada deverá ser:
#        nome -> string (poderá ser o nome ou "fim")
#       A saída deverá ser, para cada letra inicial que tem dentro do dicionário: "{letra}: {nomes}"

nomes = {}
while True:
    nome = input("Digite um nome (ou 'fim' para encerrar): ")
    if nome.lower() == "fim":
        break
    letra = nome[0].upper()
    if letra not in nomes:
        nomes[letra] = []
    nomes[letra].append(nome)

for letra in sorted(nomes.keys()):
    print(f"{letra}: {' '.join(nomes[letra])}")

# Escreva um programa que recebe uma única frase como entrada e conta quantas vezes 
# cada letra do alfabeto aparece, ignorando espaços, acentos e letras maiúsculas/minúsculas.
# Exiba as letras e suas contagens em ordem alfabética.

frase = input("Digite uma frase: ").split()
dic_contagem_letras = {}

for palavra in frase:
    for letra in palavra:
        letra = letra.upper()
        if letra.isalpha():  # Função para verificar se é uma letra do alfabeto, ignorando outros caracteres
            if letra in dic_contagem_letras:
                dic_contagem_letras[letra] += 1
            else:
                dic_contagem_letras[letra] = 1
for letra in sorted(dic_contagem_letras.keys()):
    print(f"{letra}: {dic_contagem_letras[letra]}")

# Dado um número inteiro positivo n, 
# crie um dicionário onde as chaves vão de 1 até n, e os valores são os quadrados das chaves.

n = int(input())
dic_quadradodaschaves = {}
contador = 1

while (contador <= n):
  dic_quadradodaschaves[contador] = contador ** 2
  contador += 1


for x, y in dic_quadradodaschaves.items():
	print(f"{x}: {y}")  