x = int(input("Digite o primeiro numero: "))
n = int(input("Digite o segundo numero: "))

soma = 0
cont = 0
if x and n > 0 and x < n:
    while soma < n:
        cont += 1
        soma = x * cont

print(f"O número {x} tem {cont} menores que {n}")
