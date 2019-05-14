print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42

total_de_tentativas = 3
rodada = 1

while rodada <= total_de_tentativas:
    print("Tentativa {} de {}" .format(rodada,total_de_tentativas))

    chute = int(input("Digite o seu número: "))

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Parabéns! Você acertou!")
    else:
        if maior:
            print("O seu chute foi maior que o número secreto!")
        elif menor:
            print("O seu chute foi menor que o número secreto!")

    rodada += 1

print("Fim do jogo")