
from funcoesEListas.identificacaoDeFuncoes import preencher_inventario
from funcoesEListas.identificacaoDeFuncoes import exibir_inventario
from funcoesEListas.identificacaoDeFuncoes import localizar_por_nome
from funcoesEListas.identificacaoDeFuncoes import depreciacao
from funcoesEListas.identificacaoDeFuncoes import excluir_por_serial
from funcoesEListas.identificacaoDeFuncoes import resumir_valores

minha_lista = []

print("Preenchendo")
preencher_inventario(minha_lista)

print("Exibindo")
exibir_inventario(minha_lista)

print("Pesquisando")
localizar_por_nome(minha_lista)

print("Alterando")
depreciacao(minha_lista, 20)

print("Excluindo")
print(excluir_por_serial(minha_lista))
exibir_inventario(minha_lista)

print("Resumindo")
resumir_valores(minha_lista)
