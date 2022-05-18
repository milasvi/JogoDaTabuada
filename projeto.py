from random import randint
import pygame
pygame.init()

#Efeitos
ganhei = pygame.mixer.Sound('coin.mp3.wav')
errei = pygame.mixer.Sound('errobuzz.wav')
acerteitudo = pygame.mixer.Sound('winningmusic.wav')
erreitudo = pygame.mixer.Sound('gameover.wav')

print("Bem-vinde ao JOGO da TABUADA! \nFunciona assim: Escolha a dificuldade e resolva as contas:")
dificuldade = input('Escolha a dificuldade: \n[1]Fácil \n[2]Moderado \n[3]Hardmode')

#Contadores
contador = 0
contador2 = 0

#FACIL
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
            ganhei.play()
        if int(resposta) != resolva:
            errei.play()
            print(f'Péen! Na verdade é {resolva}')

    print(f'Você acertou {contador2} vezes!')
    if int(contador2) == 5:
        acerteitudo.play()
        print('Parabéns, você acertou TODAS!!')
    elif int(contador2) < 5 and int(contador2) > 3:
        print('Você acertou quase tudo! Continue praticando!!')
    elif int(contador2) == 0:
        erreitudo.play()
        print('Uau, você conseguiu errar tudo! Tô impressionade--')
    else:
        print('Dá pra ver que multiplicação não é seu forte, mas não desista!')

        
#MODERADO
elif dificuldade == '2':
    print('Você escolheu MODERADO!')
    while contador < 7:
        contador = contador + 1
        num1 = randint(4,8)
        num2 = randint(4,8)
        resolva = num1 * num2
        resposta = input(f'{num1} x {num2} = ')
        if int(resposta) == resolva:
            ganhei.play()
            contador2 = contador2 + 1
        if int(resposta) != resolva:
            errei.play()
            print(f'Péen! Na verdade é {resolva}')
    print(f'Você acertou {contador2} vezes!')
    if int(contador2) == 7:
        acerteitudo.play()
        print('Parabéns, você acertou TODAS!!')
    elif int(contador2) < 7 and int(contador2) > 4:
        print('Você acertou quase tudo! Continue praticando!!')
    elif int(contador2) == 0:
        erreitudo.play()
        print('Uau, você conseguiu errar tudo! Tô impressionade--')
    else:
        print('Dá pra ver que multiplicação não é seu forte, mas não desista!')


#DIFICIL
elif dificuldade == '3':
    print('Você escolheu HARDMODE! \n--Apenas os corajoses escolhem esse nível--')
    while contador < 10:
        contador = contador + 1
        num1 = randint(6,12)
        num2 = randint(6,12)
        resolva = num1 * num2
        resposta = input(f'{num1} x {num2} = ')
        if int(resposta) == resolva:
            ganhei.play()
            contador2 = contador2 + 1
        if int(resposta) != resolva:
            errei.play()
            print(f'Péen! Na verdade é {resolva}')
    print(f'Você acertou {contador2} vezes!')
    if int(contador2) == 10:
        acerteitudo.play()
        print('Parabéns, você acertou TODAS!!')
    elif int(contador2) < 10 and int(contador2) > 5:
        print('Você acertou quase tudo! Continue praticando!!')
    elif int(contador2) == 0:
        erreitudo.play()
        print('Uau, você conseguiu errar tudo! Tô impressionade--')
    else:
        print('Dá pra ver que multiplicação não é seu forte, mas não desista!')


