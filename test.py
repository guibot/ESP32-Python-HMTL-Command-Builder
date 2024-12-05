# Exemplo de manipulação de strings em Python

def manipular_strings():
    # Concatenar strings
    saudacao = "Olá"
    nome = "Maria"
    mensagem = saudacao + ", " + nome + "!"
    print(mensagem)  # Saída: Olá, Maria!

    # Substituir parte da string
    nova_mensagem = mensagem.replace("Maria", "João")
    print(nova_mensagem)  # Saída: Olá, João!

    # Dividir string
    frutas = "banana, maçã, laranja"
    lista_frutas = frutas.split(", ")
    print(lista_frutas)  # Saída: ['banana', 'maçã', 'laranja']

    # Verificar presença de palavra
    if "João" in nova_mensagem:
        print("João foi encontrado na mensagem!")

    # Transformar maiúsculas/minúsculas
    texto = "python"
    print(texto.upper())  # Saída: PYTHON
    print(texto.lower())  # Saída: python

    # Remover espaços em branco
    texto_com_espacos = "   Python é incrível!   "
    print(texto_com_espacos.strip())  # Saída: Python é incrível!

    # Fatiamento de string
    print(texto[0:3])  # Saída: pyt

    # Transformar em lista de caracteres
    lista_de_caracteres = list("Python")
    print(lista_de_caracteres)  # Saída: ['P', 'y', 't', 'h', 'o', 'n']

manipular_strings()
