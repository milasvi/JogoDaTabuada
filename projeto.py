from random import randint


print("Bem-vinde ao JOGO da TABUADA! \nFunciona assim: Escolha a dificuldade e resolva as contas:")
dificuldade = input('Escolha a dificuldade: \n Fácil[1] \nModerado[2] \Hardmode[3]')
contador = 0

if dificuldade == '1':
    while contador < 5:
        contador = contador + 1
        num1 = randint(0,6)
        num2 = randint(0,6)
        resolva = num1 * num2
        resposta = input(f'{num1} x {num2}')