import sys
import os

def adicionarCartela():
    id_cartela = int(input("Insira o ID da cartela: "))
    nome = input("Insira nome do comprador: ")
    email = input("Insira o E-mail: ")
    numeros = input("Insira os numeros das cartelas: ").split()

    numeros = [eval(i) for i in numeros]
    print(numeros)

    print(nome + " foi adicionado(a)")

    doadores.append({"id": id_cartela, "nome": nome, "email": email, "numeros": numeros})

def procurarCartela():
    for doador in doadores:
        print(doador)

def procurarDoador(id_cartela):
    for doador in doadores:
        if doador['id'] == id_cartela:
            print(f"Encontrado: {doador['nome']}, email: {doador['email']} com os números {doador['numeros']}")
            return
    print(f"Doador com ID {id_cartela} não encontrado")

def salvarRegistrosTxt():
    diretorio_do_app = os.path.join(os.getcwd(), 'Projeto_Ja_Pode_Almocar')
    caminho_do_arquivo = os.path.join(diretorio_do_app, 'lista_de_doadores.txt')

    try:
        with open('lista_de_doadores.txt', 'w') as arquivo_de_doadores:
            for doador in doadores:
                linha = f"{doador['id']}, {doador['nome']},{doador['email']},{', '.join(map(str, doador['numeros']))}\n"
                arquivo_de_doadores.write(linha)

        print("Arquivo salvo com sucesso.")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

def carregarRegistroTxt():
    global doadores  
    listaDeRetorno = []

    diretorio_do_app = os.path.join(os.getcwd(), 'Projeto_Ja_Pode_Almocar')
    caminho_do_arquivo = os.path.join(diretorio_do_app, 'lista_de_doadores.txt')

    try:
        with open('lista_de_doadores.txt', 'r') as arquivo_de_doadores:
            
            for line in arquivo_de_doadores:
                doador = line.split(sep=',')
                for i in range(0, len(doador)):
                    doador[i] = doador[i].strip().replace("[", "").replace("]", "")
                listaDeRetorno.append(doador)
        doadores = []  
        for lista in listaDeRetorno:
            registroDeDoador = {"id": 0, "nome": "", "email": "", "numeros": []}
            for i in range(0, len(lista)):
                if i == 0:
                    registroDeDoador["id"] = int(lista[0])
                elif i == 1:
                    registroDeDoador["nome"] = lista[1]
                elif i == 2:
                    registroDeDoador["email"] = lista[2]
                elif i > 2:
                    registroDeDoador['numeros'].append(int(lista[i]))
            doadores.append(registroDeDoador)
        print("Arquivo carregado")
    except FileNotFoundError:
        print("O arquivo 'lista_de_doadores.txt' não foi encontrado.")
        
def encontrarGanhador():
    numeros_inseridos = []
    maior_acerto = 0
    melhor_participante = None
    while True:
        input_numeros = input("Digite os números para encontrar um ganhador (separados por espaços): ")
        novos_numeros = list(map(int, input_numeros.split()))
        numeros_inseridos.extend(novos_numeros)

        for doador in doadores:
            acertos = len(set(numeros_inseridos).intersection(set(doador['numeros'])))
            if acertos > maior_acerto:
                maior_acerto = acertos
                melhor_participante = doador['nome']

        if maior_acerto == 24: ## Insira a quantidade de numeros no bingo 
            print(f"Bingo! Temos um vencedor:")
            print(f"Ganhador: {melhor_participante} com o maior acerto de 24 números!")
            return

        print(f"A pessoa com o maior acerto até agora acertou {maior_acerto} números. Continuando...")


doadores = []
aviso = False
while True:
    if not aviso: 
        print("AVISO - CARREGUE O ARQUIVO ANTES DE TUDO!\n")
        aviso = True
    
    print(
          "1. Adicionar doador\n" +
          "2. Exibir Registro dos doadores\n" +
          "3. Procurar por um doador\n" +
          "4. Carregar Arquivo\n" +
          "5. Salvar Arquivo\n" +
          "6. Encontrar ganhador\n"
          "0. Sair")
    

    opcao = input("Digite sua escolha (0-6): ")

    if opcao == "1":
        adicionarCartela()

    elif opcao == "2":
        procurarCartela()

    elif opcao == "3":
        procurarDoador (int(input("Digite o id_cartela: ")))

    elif opcao == "5":
        confirm = input("Digite SIM para confirmar: ")
        if confirm == "Sim" or confirm == 'sim' or confirm == "S" or confirm == "s" or confirm == "SIM":
            salvarRegistrosTxt()
        else:
            print("Arquivo não foi salvo!")

    elif opcao == "4":
        carregarRegistroTxt()

    elif opcao == "6":
        encontrarGanhador()

    elif opcao == "0":
        sys.exit()

    else:
        print(f"Opção {opcao} inválida")
