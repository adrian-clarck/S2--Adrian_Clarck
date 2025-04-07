def saudacao(nome):
    if nome == "Ana":
        print("Olá, Ana! Bem-vinda.")
    elif nome == "Carlos":
        print("E aí Carlos, beleza?")
    else:
        print("Oi, prazer!")

def pedir_idade():
    idade = int(input("Quantos anos você tem? "))
    if idade < 12:
        print("Você é uma criança.")
    elif idade < 18:
        print("Você é um adolescente.")
    else:
        print("Você é um adulto.")

nome_usuario = input("Digite seu nome: ")
saudacao(nome_usuario)
pedir_idade()
