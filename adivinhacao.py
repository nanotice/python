import random

def jogar():
    print("***************************")
    print("bem vindo ao jogo de adivinhação!")
    print("***************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("qual nível de dificuldade?")
    print("(1) fácil (2) médio (3) difícil")

    nivel = int(input("defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("digite um número entre 1 e 100: ")
        print("você digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("parabéns! você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("você errou! seu chute foi maior do que o número secreto.")
            elif(menor):
                print("você errou! seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("fim do jogo")
