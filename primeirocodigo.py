# Este é um comentário. O Python ignora linhas que começam com #.
# Eles servem para explicar o que o código faz.

# 1. Pedir o nome do usuário e guardar em uma variável chamada 'nome'
nome = input("Qual é o seu nome? ")

# 2. Pedir a idade do usuário e guardar em uma variável chamada 'idade_texto'
# A função input() sempre retorna texto, mesmo que você digite um número.
idade_texto = input("Quantos anos você tem? ")

# 3. Converter a idade de texto para um número inteiro
# Isso é importante para fazer cálculos, se precisarmos.
idade = int(idade_texto)

# 4. Imprimir uma mensagem de boas-vindas
# O 'f' na frente da string permite que a gente coloque variáveis dentro das chaves {}.
print(f"Olá, {nome}! Que legal, você tem {idade} anos.")

# Você também pode adicionar um cálculo simples.
idade_em_dez_anos = idade + 10
print(f"Daqui a 10 anos, você terá {idade_em_dez_anos} anos.")