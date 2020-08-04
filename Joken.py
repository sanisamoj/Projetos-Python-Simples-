from random import randint
from time import sleep

ponto_computador = 0
ponto_jogador = 0

while ponto_computador or ponto_jogador <= 3:

    print("----Seja Bem-vindo ao Jokenpô, melhor de 3 pontos.----")
    lista = ("pedra", "papel", "tesoura", "instantaneo")
    computador = randint(0, 2)

    perguntar = int(input('''Escolha uma opcao para se jogar: 

    [0] Pedra
    [1] Papel
    [2] Tesoura

    Digite sua escolha: '''))

    print("JO\n")
    sleep(1)
    print("KEN\n")
    sleep(1)
    print("PÔÔ!!!\n")
    sleep(1)

    print("O computador escolheu: {}".format(lista[computador]))
    print("O jogador escolheu: {}".format(lista[perguntar]))

    if computador == 0:
        if perguntar == 0:
            print("Empate!")


        elif perguntar == 1:
            print("Jogador perdeu")
            ponto_computador += 1
            print("Pontos do Jogador:", ponto_jogador, " Pontos do computador:", ponto_computador)


        elif perguntar == 2:
            print("Computador venceu")
            ponto_computador += 1
            print("Pontos do Jogador:", ponto_jogador, " Pontos do computador:", ponto_computador)

        else:
            print("Operacao invalida")
            print("Pontos do Jogador:", ponto_jogador, " Pontos do computador:", ponto_computador)

    elif computador == 1:
        if perguntar == 0:
            print("Jogador perdeu")
            ponto_computador += 1
            print("Pontos do Jogador:", ponto_jogador, " Pontos do computador:", ponto_computador)

        elif perguntar == 1:
            print("Empate!")
            print("Pontos do Jogador:", ponto_jogador, " Pontos do computador:", ponto_computador)

        elif perguntar == 2:
            print("Jogador venceu")
            ponto_jogador += 1
            print("Pontos do Jogador:", ponto_jogador, " Pontos do computador:", ponto_computador)

        else:
            print("Operacao invalida")
            print("Pontos do Jogador:", ponto_jogador, " Pontos do computador:", ponto_computador)

    elif computador == 2:
        if perguntar == 0:
            print("Jogador venceu")
            ponto_jogador += 1
            print("Pontos do Jogador:", ponto_jogador, " Pontos do computador:", ponto_computador)

        elif perguntar == 1:
            print("Computador venceu")
            ponto_computador += 1
            print("Pontos do Jogador:", ponto_jogador, " Pontos do computador:", ponto_computador)

        elif perguntar == 2:
            print("Empate!")
            print("Pontos do Jogador:", ponto_jogador, " Pontos do computador:", ponto_computador)

        else:
            print("Operacao invalida")
            print("Pontos do Jogador:", ponto_jogador, " Pontos do computador:", ponto_computador)

    else:
        print("Operacao invalida")
        print("Pontos do Jogador:", ponto_jogador, " Pontos do computador:", ponto_computador)
else:
    print("Acabou")
