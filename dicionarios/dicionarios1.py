from dicionarios.Funcoes import perguntar, inserir, pesquisar, excluir, listar

equipamentos = {}
opcao = perguntar()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inserir(equipamentos)
    if opcao == "P":
        pesquisar(equipamentos, input('Qual código deseja pesquisar? '))
    if opcao == "E":
        excluir(equipamentos, input("Qual código deseja exluir? "))
    if opcao == "L":
        listar(equipamentos)

    opcao = perguntar()
