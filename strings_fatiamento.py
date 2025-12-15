# # Maiscula, Miniscula, Titulo e Capitalize

# curso = "PytHoN"

# print(curso.upper()) # vai printar "PYTHON"
# print(curso.lower()) # vai printar "python"
# print(curso.title()) # vai printar como se fosse titulo "Python"
# print(curso.capitalize()) # vai printar a primeira letra maiuscula e o resto minusculo "Python"

# # Eliminando espaços em branco 

# curso = "       Python "

# print(curso.strip()) # Remove espaços em branco da esquerda e direita "Python"
# print(curso.lstrip()) # Somente os da esquerda "Python "
# print(curso.rstrip()) # Somente os da direita "       Python"


# # Junções e Centralizações
# # .center(x , y) -Essa função recebe dois argumentos, e o seu alvo principal é apresentar a variável 
# # centralizada, por exemplo no argumento x você coloca a quantidade de caracteres desejados e no argumento y 
# # (opcional, o padrão é espaço em branco) você coloca o caractere que quer adicionar para bater a 
# # quantidade de caracteres desejado, somando a quantidade que já tem da variável com a que falta.
# # “.”.join(variável iteravel) - Essa função é para se criar junções, 
# # dentro das aspas você coloca o caractere que você quer colocar entre item a item, ou letra a letra.

# curso = "Python"

# print(curso.center(10,"#")) # Para exibir de forma centralizado com mais caracteres 
# print(".".join(curso)) # Vai juntar cada letra com o caractere colocado no join "P.y.t.h.o.n"

# # Interpolação de Iteraveis

# ## Método format ##
# nome = "Guilherme"
# idade = 28
# profissao = "Programador"
# linguagem = "Python"

# print("Olá me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome,idade,profissao,linguagem))

# # Nesse exemplo você pode printar em ordem pelo índice, e caso precise printar duplicado a variável so repetir seu indice
# print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.".format(linguagem, profissao, idade, nome))

# print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

# # usando dicionários na interpolação
# dic_pessoa = {
#     "nome":"Guilherme",
#     "idade":28,
#     "profissao":"Programador",
#     "linguagem":"Python"
# }

# print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(**dic_pessoa))

# # Método f-strings (a partir do Python 3.6)

# print(f"Olá me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

# # Fatiamento de Strings

# nome = "Guilherme Arthur de Carvalho"
# nome [0] # Vai pegar a letra G, pois o índice do texto começa em 0
# nome [:9] # Vai pegar do índice 0 até o 8, ou seja, Guilherme
# nome [10:] # Vai pegar do índice 10 até o final, ou seja, Arthur de Carvalho
# nome [10:17] # Vai pegar do índice 10 até o 16, ou seja, Arthur
# nome [10:17:2] # Vai pegar do índice 10 até o 16, sendo  Arthur, mas pulando de 2 em 2 letras, ou seja, Atur
# nome [::-1] # Vai pegar a string toda, mas de trás para frente, ou seja, ovralahC ed ruhtrA emrehliuG

# Strings triplas ou multilinhas

nome = "Israel Brito"

mensagem = f"""
    Olá meu nome é {nome},
Estou aprendendo Python
    e estou gostando muito!
"""

print(mensagem)