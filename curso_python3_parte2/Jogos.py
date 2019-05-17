import Forca
import Adivinhacao


def escolhe_jogo():
    print("*********************************")
    print("********Escolha seu jogo!********")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo? "))

    if jogo == 1:
        print("Jogando Forca")
        Forca.jogar()
    elif jogo == 2:
        print("Jogando Adivinhação")
        Adivinhacao.jogar()


if __name__ == "__main__":
    escolhe_jogo()