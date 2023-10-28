import sys

def adicionarCartela():
    id_cartela = int(input("Insira o ID da cartela: "))
    nome = input("Insira nome do comprador: ")
    numeros = input("Insira os numeros das cartelas: ").split()

    numeros = [eval(i) for i in numeros]
    print(numeros)

    print(nome + " foi adicionado(a)")

    doadores.append({"id": id_cartela, "nome": nome, "numeros": numeros})

def procurarCartela():
    for doador in doadores:
        print(doador)

def procurarDoador(id_cartela):
    for doador in doadores:
        if doador['id'] == id_cartela:
            print(f"Encontrado: {doador['nome']} com os números {doador['numeros']}")
            return
    print(f"Doador com ID {id_cartela} não encontrado")

def salvarRegistrosTxt():
    with open('lista_de_doadores.txt', 'w') as arquivo_de_doadores:
        for doador in doadores:
            arquivo_de_doadores.write(f"{doador['id']}, {doador['nome']}, {', '.join(map(str, doador['numeros']))}\n")

def carregarRegistroTxt():
    listaDeRetorno = []
    with open('lista_doadores.txt') as arquivo_de_doadores:
        for line in arquivo_de_doadores:
         doador = line.split(sep=',')
        for i in range(0, len(doador)):
            doador[i] = doador[i].strip().replace("[", "").replace("]", "")
            listaDeRetorno.append (doador)

    for lista in listaDeRetorno:
        registroDeAluno = {"id": 0, "nome": "", "numeros": []}
        for i in range(0, len(lista)):
            if i == 0:
                registroDeAluno["id"] = int(lista[0])
            elif i == 1:
                registroDeAluno["nome"] = lista[1]
            elif i > 1:
                registroDeAluno['numeros'].append(int(lista[i]))
        doadores.append(registroDeAluno)
    print("Arquivo carregado")

def encontrarGanhador():
    numeros_inseridos = input("Digite os números para encontrar um ganhador (separados por espaços): ").split()
    numeros_inseridos = [int(numero) for numero in numeros_inseridos]
    
    for doador in doadores:
        if set(numeros_inseridos).issubset(set(doador['numeros'])):
            print(f"Ganhador: {doador['nome']} com os números {doador['numeros']}")
            return
    print(f"Nenhum ganhador encontrado com os números inseridos.")
doadores = []
while True:
    print(
          "1. Adicionar doador\n" +
          "2. Exibir Registro dos doadores\n" +
          "3. Procurar por um doador\n" +
          "4. Salvar Arquivo\n" +
          "5. Carregar Arquivo\n" +
          "6. Encontrar ganhador\n"
          "0. Sair")

    opcao = input("Digite sua escolha (0-6): ")

    if opcao == "1":
        adicionarCartela()
    elif opcao == "2":
        procurarCartela()
    elif opcao == "3":
        procurarDoador (int(input("Digite o id_cartela: ")))
    elif opcao == "4":
        salvarRegistrosTxt()
    elif opcao == "5":
        carregarRegistroTxt()
    elif opcao == "6":
        encontrarGanhador()
    elif opcao == "0":
        sys.exit()
    else:
        print(f"Opção {opcao} inválida")
