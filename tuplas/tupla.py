ips = {}
resp = "S"

while resp == "S":
    ips[(input("DIgite os dois primeiros octetos: "),
        input("Digite os dois últimos octetos: "))] = input("Nome da maquina:")
    resp = input("Digite <S> para continuar: ").upper()

print("Exibindo máquinas com o mesmo endereço: ")

pesquisa = input("Digite os dois últimos octetos: ")

for ip, nome in ips.items():
    print("Máquinas no mesmo endereço (redes diferentes): ")
    if (ip[1] == pesquisa):
        print(nome)

print("Exibindo as máquinas que compões uma mesma rede: ")
rede = input("DIgite os oids primeiros octetos: ")
for ip, nome in ips.items():
    if(ip[0] == rede):
        print(nome)
