def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_chave = "banana"
    enforcou = False
    acertou = False
    letras_acertadas = []

    count = len(palavra_chave)

    for i in range(1,len(palavra_chave) + 1):
        letras_acertadas.append("_")

    print(letras_acertadas)

    while not acertou and not enforcou:


        chute = input("Qual letra? ")
        chute = chute.strip()

        index = 0

        for letra in palavra_chave:
            if chute.upper() == letra.upper():
                letras_acertadas[index] = chute
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1


        if (not "_" in letras_acertadas):
            acertou = True

        print(letras_acertadas)

    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
