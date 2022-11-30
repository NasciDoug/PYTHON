print("*********************************")
print("Bm vindo ao jogo de adivinhação!!")
print("*********************************")

num_secreto = 42
tentativa_total = 3
tentativa = 1

while(tentativa<=tentativa_total):
    print("\nTentativa {} de {}".format(tentativa, tentativa_total))
    palpite_str=input ("Digite o seu papite (número): ")

    print("Você digitou: ", palpite_str)
    palpite = int(palpite_str)

    acertou = palpite == num_secreto
    maior = palpite > num_secreto

    if (acertou):
        print("Você acertou!!")
    else:
        if(maior):
            print("Você errou, seu palpite foi mais alto!!")
        else:
            print("Você errou, seu palpite foi menor!!")
    tentativa+=1

print("\nFim do jogo!!")


