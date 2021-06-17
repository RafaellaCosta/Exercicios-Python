def perguntar():
    resposta = input("""O que deseja realizar? " +
            "<I> - Para Inserir um equipamento" +
            "<P> - Para Pesquisar um equipamento" +
            "<E> - Para Excluir um equipamento" +
            "<L> - Para Listar equipamentos: """).upper()
    return resposta


def inserir(dicionario):
    dicionario[input("Digite o código: ").upper()] = [input(
            "Digite o nome do equipamentos: ").upper(), input(
                "Digite data da compra: "), input(
                    "Qual foi o ultimo dia utilizado: ").upper()]


def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista is not None:
        print('Nome..................: ' + lista[0])
        print('Data aquisição........: ' + lista[1])
        print('Ultimo dia utilizado..: ' + lista[2])


def excluir(dicionario, chave):
    if dicionario.get(chave) is not None:
        del dicionario[chave]
    print('Equipamento eliminado')


def listar(dicionario):
    for chave, valor in dicionario.items():
        print('Equipamento....')
        print('Código: ', chave)
        print('Dados: ', valor)
