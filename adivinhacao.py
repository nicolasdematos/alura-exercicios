from random import *
def play():
    r = randint(1, 100)
    difficult = int(input('Escolha uma dificultade \n\nfacil[1]\nmedio[2]\ndificil[3]\n>>>'))
    print('chute um número de 1 a 100')
    if difficult == 1:
        tries = 10
    elif difficult == 2:
        tries = 5
    elif difficult == 3:
        tries = 3
    else:
        print('valor errado!')
    while tries > 0:
        n = int(input('>>>'))
        if n != r:
            if n > r:
                print('um pouco menor!')
            else:
                print('um pouco maior!')
        else:
            print('numero certo!')
            break
        tries -= 1
        if tries == 0:
            print('Suas tentativas acabaram!')
            print(f'O número correto era {r}')
            break

if __name__ == "__main__":
    play()