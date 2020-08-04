from random import randint

def jogar_fácil():
    print('*' * 20)
    print('Jogo da advinhação com 8 Tentativas!')
    print('*' * 20)

    numero_de_tentativas = 8
    numero_secreto = randint(0, 33)

    while numero_de_tentativas >= 1:
        chute = int(input('Você tem {} tentativas! Chute um número entre 0 e 33: '.format(numero_de_tentativas)))
        numero_de_tentativas -= 1

        if chute == numero_secreto:
            print('Uau , você acertou o número secreto \n o seu número foi: {} e o número secreto é: {}'.format(chute,
                                                                                                                numero_secreto))
            break

        elif chute < numero_secreto:
            print('Quase , você digitou o número {} , tente um número maior!'.format(chute))

        elif chute > numero_secreto:
            print('Quase , você digitou o número {} , tente um número menor!'.format(chute))

    else:
        print("Infelizmente você excedeu as tentativas")

def jogar_médio():
    print('*' * 20)
    print('Jogo da advinhação com 5 Tentativas!')
    print('*' * 20)

    numero_de_tentativas = 5
    numero_secreto = randint(0, 33)

    while numero_de_tentativas >= 1:
        chute = int(input('Você tem {} tentativas! Chute um número entre 0 e 33: '.format(numero_de_tentativas)))
        numero_de_tentativas -= 1

        if chute == numero_secreto:
            print('Uau , você acertou o número secreto \n o seu número foi: {} e o número secreto é: {}'.format(chute,
                                                                                                                numero_secreto))
            break

        elif chute < numero_secreto:
            print('Quase , você digitou o número {} , tente um número maior!'.format(chute))

        elif chute > numero_secreto:
            print('Quase , você digitou o número {} , tente um número menor!'.format(chute))

    else:
        print("Infelizmente você excedeu as tentativas")

def jogar_difícil():
    print('*' * 20)
    print('Jogo da advinhação com 3 Tentativas!')
    print('*' * 20)

    numero_de_tentativas = 3
    numero_secreto = randint(0, 33)

    while numero_de_tentativas >= 1:
        chute = int(input('Você tem {} tentativas! Chute um número entre 0 e 33: '.format(numero_de_tentativas)))
        numero_de_tentativas -= 1

        if chute == numero_secreto:
            print('Uau , você acertou o número secreto \n o seu número foi: {} e o número secreto é: {}'.format(chute,
                                                                                                                numero_secreto))
            break

        elif chute < numero_secreto:
            print('Quase , você digitou o número {} , tente um número maior!'.format(chute))

        elif chute > numero_secreto:
            print('Quase , você digitou o número {} , tente um número menor!'.format(chute))

    else:
        print("Infelizmente você excedeu as tentativas")

def iniciar_jogo():
    print('*' * 20)
    print('Jogo da Advinhação')
    print('*' * 20)

    escolha = int(input('O jogo consiste em advinhar um número entre 0 e 33\n'
                        'Digite [1] Para o modo fácil com 8 tentativas!\n'
                        'Digite [2] Para o modo Médio com 5 tentativas!\n'
                        'Digite [3] Para o modo Difícil com 3 tentativas!\n'
                        'Digite qualquer outro número para sair do jogo!\n'
                        '********************\n'
                        'Digite sua escolha : '))

    if escolha == 1:
        jogar_fácil()
    elif escolha == 2:
        jogar_médio()
    elif escolha == 3:
        jogar_difícil()
    else:
        exit()


iniciar_jogo()
