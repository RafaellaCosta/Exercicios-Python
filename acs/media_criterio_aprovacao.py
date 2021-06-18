n_1 = float(input("Digite a nota 1: "))
n_2 = float(input("Digite a nota 2: "))
n_3 = float(input("Digite a nota 3: "))
freq = float(input("Digite a frequência de 0 até 1: "))

media = ((n_1 * 2) + (n_2 * 2) + (n_3 * 3)) / (2 + 2 + 3)
m_arrend = round(media, 1)

if m_arrend > 9:
    if (freq * 100) >= 75:
        print(f"""
                Frequencia: {freq}%
                Media final: {m_arrend}
                Aluno aprovado com louvor!""")
    else:
        print("Aluno repovado por falta!")

if m_arrend >= 6 and m_arrend <= 9:
    if (freq * 100) >= 75:
        print(f"""
                Frequencia: {freq}%
                Media final: {m_arrend}
                Aluno aprovado!!""")
    else:
        print("Aluno repovado por falta!")

if m_arrend >= 4 and m_arrend < 6:
    if (freq * 100) >= 75:
        print(f"""
                Frequencia: {freq}%
                Media final: {m_arrend}
                Aluno de rec!""")
    else:
        print("Aluno repovado por falta!")

if m_arrend < 4:
    if (freq * 100) >= 75:
        print(f"""
                Frequencia: {freq}%
                Media final: {m_arrend}
                Aluno de reprovado!""")
    else:
        print("Aluno repovado por falta!")
