from random import randint


print("Bem-vinde ao JOGO da TABUADA! \nFunciona assim: Escolha a dificuldade e resolva as contas:")
dificuldade = input('Escolha a dificuldade: \nFácil[1] \nModerado[2] \nHardmode[3]')
contador = 0
contador2 = 0

if dificuldade == '1':
    print('Você escolheu FÁCIL: \n')
    while contador < 5:
        contador = contador + 1
        num1 = randint(0,6)
        num2 = randint(0,6)
        resposta = input(f'{num1} x {num2} = ')
        resolva = num1 * num2
        if int(resposta) == resolva:
            contador2 = contador2 + 1
        if int(resposta) != resolva:
            print(f'Péen! Na verdade é {resolva}')
    print(f'Você acertou {contador2} vezes!')
    if int(contador2) == 5:
        print('Parabéns, você acertou TODAS!!')
    elif int(contador2) < 5 and int(contador2) > 3:
        print('Você acertou quase tudo! Continue praticando!!')
    elif int(contador2) == 0:
        print('Uau, você conseguiu errar tudo! Tô impressionade--')
    else:
        print('Dá pra ver que multiplicação não é seu forte, mas não desista!')

        

elif dificuldade == '2':
    print('Você escolheu MODERADO!')
    while contador < 7:
        contador = contador + 1
        num1 = randint(4,8)
        num2 = randint(4,8)
        resolva = num1 * num2
        resposta = input(f'{num1} x {num2} = ')
        if int(resposta) == resolva:
            contador2 = contador2 + 1
        if int(resposta) != resolva:
            print(f'Péen! Na verdade é {resolva}')
    print(f'Você acertou {contador2} vezes!')
    if int(contador2) == 7:
        print('Parabéns, você acertou TODAS!!')
    elif int(contador2) < 7 and int(contador2) > 4:
        print('Você acertou quase tudo! Continue praticando!!')
    elif int(contador2) == 0:
        print('Uau, você conseguiu errar tudo! Tô impressionade--')
    else:
        print('Dá pra ver que multiplicação não é seu forte, mas não desista!')


elif dificuldade == '3':
    print('Você escolheu HARDMODE! \n--Apenas os corajoses escolhem esse nível--')
    while contador < 10:
        contador = contador + 1
        num1 = randint(6,12)
        num2 = randint(6,12)
        resolva = num1 * num2
        resposta = input(f'{num1} x {num2} = ')
        if int(resposta) == resolva:
            contador2 = contador2 + 1
        if int(resposta) != resolva:
            print(f'Péen! Na verdade é {resolva}')
    print(f'Você acertou {contador2} vezes!')
    if int(contador2) == 10:
        print('Parabéns, você acertou TODAS!!')
    elif int(contador2) < 10 and int(contador2) > 5:
        print('Você acertou quase tudo! Continue praticando!!')
    elif int(contador2) == 0:
        print('Uau, você conseguiu errar tudo! Tô impressionade--')
    else:
        print('Dá pra ver que multiplicação não é seu forte, mas não desista!')


