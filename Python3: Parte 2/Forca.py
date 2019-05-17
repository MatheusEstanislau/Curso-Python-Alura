def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_chave = "banana"
    letras_acertadas = []

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for i in range(1, len(palavra_chave) + 1):
        letras_acertadas.append("_")

    print(letras_acertadas)

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = input("Digite um numero entre 1 e 100: ")

        index = 0

        for letra in palavra_chave:
            if chute.upper() == letra.upper():
                letras_acertadas[index] = chute
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1

        if "_" not in letras_acertadas:
            print("Parabéns você acertou!")
            break

        print(letras_acertadas)

    print("Que pena você perdeu! A palavra secreta era {}".format(palavra_chave.upper()))


if __name__ == "__main__":
    jogar()
