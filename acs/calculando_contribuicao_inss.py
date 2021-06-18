salario_base = float(input("Digite seu salário: ").replace(",", "."))

if salario_base <= 1751.81:
    soma = salario_base * 0.08
    print(f"Desconto do INSS: R$ {soma:.2f}")

if salario_base >= 1751.82 and salario_base <= 2919.72:
    soma = salario_base * 0.09
    print(f"Desconto do INSS: R$ {soma:.2f}")

if salario_base >= 2919.73:
    soma = salario_base * 0.11
    print(f"Desconto do INSS: R$ {soma:.2f}")
