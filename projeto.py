from random import randint


print("Bem-vinde ao JOGO da TABUADA! \nFunciona assim: Escolha a dificuldade e resolva as contas:")
dificuldade = input('Escolha a dificuldade: \nFácil[1] \nModerado[2] \nHardmode[3]')
contador = 0
contador2 = 0

if dificuldade == '1':

    while contador < 3:
        contador = contador + 1
        num1 = randint(0,6)
        num2 = randint(0,6)
        resposta = input(f'{num1} x {num2} = ')
        resolva = num1 * num2
        if int(resposta) == resolva:
            contador2 = contador2 + 1
    print(f'Você acertou {contador2} vezes!')
        

elif dificuldade == '2':
    while contador < 7:
        contador = contador + 1
        num1 = randint(6,8)
        num2 = randint(6,8)
        resolva = num1 * num2
        resposta = input(f'{num1} x {num2} = ')
elif dificuldade == '3':
    while contador > 12:
        contador = contador + 1
        num1 = randint(8,12)
        num2 = randint(8,12)
        resolva = num1 * num2
        resposta = input(f'{num1} x {num2} = ')

