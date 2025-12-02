'''
Faça um programa que, dado um valor n, exiba os valores de 0 a n que são múltiplos de 3, de 5 e de ambos.
'''

n = int(input("Digite um valor para n: "))
for i in range(0,n+1):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i} é múltiplo de 3 e de 5")
    elif i % 3 == 0:
        print(f"{i} é múltiplo de 3")
    elif i % 5 == 0:
        print(f"{i} é múltiplo de 5")  
        
'''
Faça um programa que, dado um número, faça a contagem regressiva até 0 
para saber a hora do lançamento de um foguete
'''

n = int(input("Digite um número para a contagem regressiva: "))
for i in range(n, -1, -1):
    print(i)
print("O foguete decolou!")

'''
Faça um programa para ler o primeiro e último número de uma sequência e depois exibir: a somatória desses dois números, os números pares e os números ímpares dentro desse intervalo da sequência.
'''

primeiro = int(input("Digite o primeiro número da sequência: "))
segundo = int(input("Digite o segundo número da sequência: "))

soma = primeiro + segundo

print(f"A soma dos números é: {soma}\n")

print("Os números pares dentro da sequência são:")
for i in range(primeiro, segundo + 1):
    if i % 2 == 0:
        print(i)

print("\nOs números ímpares dentro da sequência são:")
for i in range(primeiro, segundo + 1):
    if i % 2 != 0:
        print(i)

'''
Escreva um programa que, dado um valor n, escreva a tabuada desse número (n x 1 até n x 10)
'''
n = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 11):
    resultado = n * i
    print(f"{n} x {i} = {resultado}")

'''
A sequência de Fibonacci é uma famosa sequência numérica onde cada número é a soma dos dois anteriores. Ela começa com os termos 0 e 1, e segue assim:

0, 1, 1, 2, 3, 5, 8, 13, 21, ...

Ou seja:

O 0º termo é 0
O 1º termo é 1
A partir do 2º termo: F(n) = F(n-1) + F(n-2)
Faça um programa que, dado um número inteiro n, imprima todos os termos da sequência de Fibonacci menores ou iguais a n, linha a linha.
'''

termo = int(input())

a, b = 0, 1
print(a)
while b <= termo:
    print(b)
    a, b = b, a + b

'''
Faça um programa para ler números inteiros e positivos até o usuário não desejar continuar informando um novo número. 
Ao final, o programa deve exibir o total de números lidos e a soma deles.
'''

quantidade = 0
soma = 0
confirmacao = str(input("Deseja digitar um numero? (s/n)"))

while confirmacao != "n":
    numero = float(input("Digite um número inteiro e positivo: "))
    if numero > 0:
        quantidade += 1
        soma += numero
    confirmacao = str(input("Deseja digitar um numero? (s/n)"))
    
print(f"Você digitou {quantidade} números")
print(f"A soma final é: {soma:.2f}")

'''
Faça um programa que receba dois valores inteiros (a e b), 
e faça a divisão de a por b SEM UTILIZAR o operador / ou //.

Obs.: considere sempre que a >= b
'''

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
quociente = 0

while a >= b:
    a -= b
    quociente += 1 

print(f"O quociente da divisão é: {quociente}")
print(f"O resto da divisão é: {a}")    

'''
Escreva um programa que, dado um inteiro N, imprimir a sequência de Collatz
começando com N até que o número chegue a 1. Cada número da sequência deve ser impresso em uma nova linha.

A Sequência de Collatz é da seguinte forma:

Se o número for par, divida-o por 2.
Se o número for ímpar, multiplique-o por 3 e adicione 1.
'''

n = int(input())

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    print(n)
    
'''
Escreva um programa que recebe um número inteiro n e imprime Sim se ele for um número primo, ou Não caso contrário.

Input

A entrada será da seguinte forma:

n -> inteiro

Output

A saída deverá ser:

Se o número for primo:

"Sim, esse número é primo"

Caso contrário:

"O número não é primo"
'''

n = int(input())

if n % 1 == 0 and n % n == 0 and n > 1 and n % 2 != 0:
    print("Sim, esse número é primo")
else:
    print("O número não é primo")