import random


def sorteio1():
    num = random.randint(1, 10)
    while True:

        try:
            resp = int(input("digite"))
            if not 0 <= resp <= 10:
                raise ValueError("Nota fora do range permitido")
        except ValueError as e:
            print("Valor inválido:", e)
        else:
            if resp < num:
                print('mais pra cima')
            elif resp > num:
                print('Mais para Baixo')
            else:
                print("Parabens !! Voce acertou  o numero era ", num)
                break
                return False


def sorteio2():
    num = random.randint(1, 20)
    while True:

        try:
            resp = int(input("digite"))
            if not 0 <= resp <= 30:
                raise ValueError("Nota fora do range permitido")
        except ValueError as e:
            print("Valor inválido:", e)
        else:
            if resp < num:
                print('mais pra cima')
            elif resp > num:
                print('Mais para Baixo')
            else:
                print("Parabens !! Voce acertou  o numero era ", num)
                break
                return False


def sorteio3():
    num = random.randint(1, 30)
    while True:

        try:
            resp = int(input("digite"))
            if not 0 <= resp <= 30:
                raise ValueError("Nota fora do range permitido")
        except ValueError as e:
            print("Valor inválido:", e)
        else:
            if resp < num:
                print('mais pra cima')
            elif resp > num:
                print('Mais para Baixo')
            else:
                print("Parabens !! Voce acertou  o numero era ", num)
                break


while True:
    print("Escolha um nivel")
    print("1-Facil")
    print("2-Normal")
    print("3-Dificil")
    niv = int(input("Escolha um Nivel"))
    if niv == 1:
        sorteio1()
        break
    elif niv == 2:
        sorteio2()
        break

    elif niv == 3:
        break
    else:
        print("Valor nao existe")
