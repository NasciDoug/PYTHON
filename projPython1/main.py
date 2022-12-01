import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!!")
    print("*********************************")

    num_secreto = random.randrange(1,101)
    tentativa_total = 0
    pontos = 100

    print("Qual nível de dificuldade você escolhe?")
    print("(1) Fáicl\n(2) Médio\n(3) Difícil")
    nivel = int(input("Defina o nível: "))

    if(nivel==1):
        tentativa_total = 8
    elif(nivel==2):
        tentativa_total = 5
    else:
        tentativa_total = 3

    for rodada in range(1, tentativa_total+1):
        print("\nTentativa {} de {}".format(rodada, tentativa_total))
        palpite_str=input ("Digite o seu papite (número entre 1 e 100): ")

        print("Você digitou: ", palpite_str)
        palpite = int(palpite_str)

        if (palpite<1 or palpite>100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = palpite == num_secreto
        maior = palpite > num_secreto

        if (acertou):
            print("Você acertou!!")
            break
        else:
            if(maior):
                print("Você errou, seu palpite foi mais alto!!")
            else:
                print("Você errou, seu palpite foi menor!!")

            pontos -=abs(num_secreto-palpite)
            print("pontos restantes: {}".format(pontos))

    print("\nFim do jogo!!, o número era {}!!!".format(num_secreto))

if (__name__ == "__main__"):
    jogar()