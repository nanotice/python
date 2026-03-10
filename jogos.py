import forca
import adivinhacao

print("*****************")
print("escolhe seu jogo!")
print("*****************")

print("(1) forca (2) adivinhação")

jogo = int(input("qual jogo? "))

if(jogo == 1):
    print("jogando forca")
    forca.jogar()
elif(jogo == 2):
    print("jogando adivinhação")
    adivinhacao.jogar()