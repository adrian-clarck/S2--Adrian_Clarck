def saudacao(nome):
    if nome == "Ana":
        print("Olá, Ana! Bem-vinda.")
    elif nome == "Carlos":
        print("E aí Carlos, beleza?")
    else:
        print("Oi, prazer!")

nome_usuario = input("Digite seu nome: ")
saudacao(nome_usuario)
