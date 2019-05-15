import random


print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = random.randrange(0,101) # gera número entre 0.0

total_de_tentativas = 10
rodada = 1

for rodada in range(1, total_de_tentativas + 1):
    print(numero_secreto)
    print("Tentativa {} de {}" .format(rodada, total_de_tentativas))
    chute = int(input("Digite um numero entre 1 e 100: "))

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100! ")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Parabéns! Você acertou!")
        break
    else:
        if maior:
            print("O seu chute foi maior que o número secreto!")
        elif menor:
            print("O seu chute foi menor que o número secreto!")

print("Fim do jogo")

