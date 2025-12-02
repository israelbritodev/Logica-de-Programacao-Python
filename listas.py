# # Faça um programa que receba 10 números digitados pelo usuário e, em seguida, 
# # leia um expoente. O programa deve criar e imprimir uma nova lista com cada número elevado 
# # ao expoente informado.

# Criação da lista vazia para armazenar os números
numeros = []

# Loop para receber 10 números do usuário
for i in range(10):
    # Solicita ao usuário que digite um número inteiro
    numero = int(input("Digite um número inteiro: "))
    # Adiciona o número à lista
    numeros.append(numero)
    
# Solicita ao usuário que digite o expoente
expoente = int(input("Digite o expoente: "))

# Criação da nova lista em branco
numeros_elevados = []

# Loop para elevar cada número ao expoente(**) e adicionar à nova lista usando o append
for x in numeros:
    numeros_elevados.append(x ** expoente)

# Exibe a nova lista
for a in numeros_elevados:
    print(f"{a:.2f}")
    
# '''
# Faça um programa que leia o nome e a nota de vários alunos (a entrada termina quando for digitado um 
# nome vazio OU quando a entrada for "fim"). Armazene os nomes em uma lista e as notas em outra.
# Em seguida, exiba os nomes dos alunos ordenados da maior para a menor nota.
# '''

nomes_alunos = []
notas_alunos = []
alunos_e_notas = {}
nome_aluno = " "

while (nome_aluno != "") and (nome_aluno.lower() != "fim"):
    nome_aluno = str(input("Digite o nome do aluno: "))
    if (nome_aluno != "") and (nome_aluno.lower() != "fim") and (nome_aluno not in nomes_alunos):
        nota_aluno = float(input("Digite a nota do aluno: "))
        nomes_alunos.append(nome_aluno)
        notas_alunos.append(nota_aluno)


for nome, nota in zip(nomes_alunos, notas_alunos):
    alunos_e_notas[nome] = nota

for nome, nota in sorted(alunos_e_notas.items(), key=lambda item: item[1], reverse=True):
    print(f"{nome}: {nota:.2f}")
    
'''
Dada uma lista de n números, calcule a média aritmética e conte quantos elementos são maiores do que ela.
'''

elementos = input("Digite os números separados por espaço em branco: ").split()
qtd_numero_maior_media = 0

for numero in map(int, elementos):
    media = sum(map(int, elementos)) / len(elementos)
    if (numero > media):
      qtd_numero_maior_media += 1

print(qtd_numero_maior_media)


#  Escreva um programa em Python que permita ao usuário digitar uma quantidade indeterminada de números inteiros, um por vez.
#  Depois, o programa deverá exibir a quantidade de números digitados, a quantidade de números pares e a quantidade de números ímpares.


#Declarando as variaveis
confirmacao = "s"
numeros = []
numero = 0
soma_pares = 0
soma_impares = 0

#enquanto confirmacao for igual a s (sim) ele executa
while (confirmacao == "s"):
  # recebe o numero
  numero = (input("Digite um número: "))
  # adiciona a lista de numeros
  numeros.append(numero)
  # confirma se o usuário deseja digitar mais outro número
  confirmacao = input("Deseja continuar? [s/n] ").lower()
# caso a confirmacao for diferente de s(sim)
else:
  # para cada x dentro da lista de numeros
  for x in map(int, numeros):
    # se x for divisivel por 2 (par)
    if (x % 2 == 0):
      # a variavel soma_pares soma o numero anteriormente adicionado ao numero novo
      soma_pares = soma_pares + x
    else:
      # se for ímpar
      soma_impares = soma_impares + x
  # pega a quantidade total de números através da função len
  qtd_total = len(numeros)
  # mostrar tudo ao usuário
  print(f"Quantidade de números digitados: {qtd_total}")
  print(f"Soma dos números pares: {soma_pares}")
  print(f"Soma dos números ímpares: {soma_impares}")


# Faça um programa que leia os nomes (sem repetição),
# os preços de compra e os percentuais de lucro de 5 produtos. Após a leitura, exiba para cada produto 
# seu nome, o preço de compra e o preço de venda calculado.

# Declarando as listas globais
nomes_produto = []
preco_compra = []
preco_venda = []

# Para cada i no range de 5 (5 produtos)
for i in range(5):
    # Adiciona o nome do produto na lista nomes_produto
  nomes_produto.append(input("Digite o nome do produto: "))
    # Adiciona o preço de compra na lista preco_compra
  preco_compra.append(float(input("Digite o preço de compra: ")))
  
    # Calcula o preço de venda e adiciona na lista preco_venda
  percentual_lucro = float(input("Digite o percentual de lucro: "))
  preco_venda.append(preco_compra[-1] + (preco_compra[-1] * (percentual_lucro / 100)))
  
# Exibe os resultados 
for i in range(5):
  print(f"{nomes_produto[i]}: Compra = R${preco_compra[i]:.2f}, Venda = R${preco_venda[i]:.2f}")
  

# Escreva um programa que recebe valores para serem adicionados numa lista. 
# Após isso, o programa deverá exibir quantas vezes os valores aparecem dentro da lista.

#Declarando as variaveis
confirmacao = "s"
numeros = []
n = 0.0

while (confirmacao == "s"):
  # recebe o numero
  n = float(input("Digite um número: "))
  # adiciona a lista de numeros
  numeros.append(n)
  # confirma se o usuário deseja digitar mais outro número
  confirmacao = input("Deseja continuar? [s/n] ").lower()

vistos = set()

for x in numeros:
    if x not in vistos:
        quantidade = numeros.count(x)
        print(f"O elemento {x} aparece {quantidade} vezes na lista")
        vistos.add(x)

# Dada uma lista de números inteiros distintos, escreva um programa que encontre o n-ésimo maior valor da lista.
# O programa deve primeiro ler um inteiro t (tamanho da lista), depois t inteiros distintos n, e por fim um inteiro k, representando a posição do valor desejado na ordem crescente.

t = int(input("Digite o tamanho da lista: "))
n = []

for i in range(t):
    n.append(int(input("Digite o número desejado:")))
    
k = int(input("Digite a posição: "))

n.sort()

descobrindo_valor = n[k]

print(descobrindo_valor)    

# Dada uma lista de n números inteiros e um valor inteiro k, crie uma nova lista com os elementos multiplicados por k e imprima o resultado.
# Os elementos da lista devem ser recebidos em uma única linha, separados por um espaço em branco, e devem ser convertidos para inteiro posteriormente.
# Obs.: existe um espaço final em branco após a exibição do último elemento.
# Output
# A saída deverá ser os elementos da nova lista, multiplicados por k, na mesma linha, separados por um espaço em branco entre eles.

elementos = input("Digite os números separados por espaço em branco: ").split()
k = int(input("Digite o valor de k: "))

nova_lista = []

for numero in map(int, elementos):
    nova_lista.append(numero * k)

for v in nova_lista:
    print(v, end=' ')
print()

