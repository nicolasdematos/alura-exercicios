import adivinhacao
import forca

escolha = int(input('digite qual voce quer jogar\n\n1-adivinhacao\n2-forca'))

if escolha == 1:
    adivinhacao.play()
elif escolha == 2:
    forca.play()
else:
    print('Escolha invalida!')