print("************************************")
print("bem vindo ao jogo de adivinhação!")
print("************************************")

numero_secreto = 42
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas +1):
    print("tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("digite um número entre 1 e 100: ")
    print("você digitou", chute_str)
    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("você deve digitar um número entre 1 e 100!!!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("parabéns, você acertou!")
        break
    else:
        if(maior):
            print("você errou! o seu chute foi maior do que o número secreto.")
        elif(menor):
             print("você errou! o seu chute foi menor do que o número secreto.")

print("fim de jogo")