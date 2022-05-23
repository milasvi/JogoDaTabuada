from codecs import replace_errors
from logging import captureWarnings
from random import randint
from time import sleep
import pygame
import emoji
pygame.init()

#Efeitos
ganhei = pygame.mixer.Sound('ProjetodaTabuada\musica\coin.mp3.wav')
errei = pygame.mixer.Sound('ProjetodaTabuada\musica\errobuzz.wav')
acerteitudo = pygame.mixer.Sound('ProjetodaTabuada\musica\winningmusic.wav')
erreitudo = pygame.mixer.Sound('ProjetodaTabuada\musica\gameover.wav')
interface = pygame.mixer.Sound('ProjetodaTabuada\musica\interface.wav')

#cabecalho
print('=--'* 12)
print(emoji.emojize(':multiply:  Bem-vinde ao JOGO da TABUADA!:multiply:'))
print('=--'* 12)
print('Funciona assim: Escolha a dificuldade e resolva as contas:')

#Contadores
contador1 = 0
contador2 = 0
contador3 = 0

#JOGO

while True:
    interface.play()
    dificuldade = input('Escolha a dificuldade: \n\033[0;36m[1]Fácil\033[m \n\033[0;34m[2]Moderado\033[m \n\033[0;35m[3]Hardmode\033[m ')
    #FACIL
    if dificuldade == '1':
        print('Você escolheu FÁCIL: \n')
        for _ in range(5):
            num1 = randint(0,6)
            num2 = randint(0,6)
            resposta = input(f'{num1} x {num2} = ')
            resolva = num1 * num2
                
            if int(resposta) == resolva:
                contador1 += 1
                ganhei.play()
            if int(resposta) != resolva:
                errei.play()
                print(f'Péen! Na verdade é {resolva}')

        print(f'Você acertou {contador1} vezes!')
        if int(contador1) == 5:
            acerteitudo.play()
            print(emoji.emojize(':1st_place_medal: Parabéns, você acertou TODAS!!:partying_face: :party_popper:'))
            sleep(2)
        elif int(contador1) < 5 and int(contador2) > 3:
            print(emoji.emojize(':2nd_place_medal: Você acertou quase tudo! Continue praticando!!'))
        elif int(contador1) == 0:
            erreitudo.play()
            print(emoji.emojize('Uau, você conseguiu errar tudo! Tô impressionade--:frowning_face:'))
            sleep(2)
        else:
            print(emoji.emojize(':3rd_place_medal: Dá pra ver que multiplicação não é seu forte, mas não desista!'))

            
    #MODERADO
    elif dificuldade == '2':
        print('Você escolheu MODERADO!')
        for _ in range(7):
            num1 = randint(4,8)
            num2 = randint(4,8)
            resolva = num1 * num2
            resposta = input(f'{num1} x {num2} = ')
            if int(resposta) == resolva:
                ganhei.play()
                contador2 += 1
            if int(resposta) != resolva:
                errei.play()
                print(f'Péen! Na verdade é {resolva}')
        print(f'Você acertou {contador2} vezes!')
        if int(contador2) == 7:
            acerteitudo.play()
            print(emoji.emojize(':1st_place_medal: Parabéns, você acertou TODAS!!:partying_face: :party_popper:'))
            sleep(2)
        elif int(contador2) < 7 and int(contador2) > 4:
            print(emoji.emojize(':2nd_place_medal: Você acertou quase tudo! Continue praticando!!'))
        elif int(contador2) == 0:
            ganhei.play()
            print(emoji.emojize('Uau, você conseguiu errar tudo! Tô impressionade--:frowning_face:'))
            sleep(2)
        else:
            print(emoji.emojize(':3rd_place_medal: Dá pra ver que multiplicação não é seu forte, mas não desista!'))


    #DIFICIL
    elif dificuldade == '3':
        print('Você escolheu HARDMODE! \n--Apenas os corajoses escolhem esse nível--')
        for _ in range(10):
            num1 = randint(6,12)
            num2 = randint(6,12)
            resolva = num1 * num2
            resposta = input(f'{num1} x {num2} = ')
            if int(resposta) == resolva:
                ganhei.play()
                contador3 += 1
            if int(resposta) != resolva:
                errei.play()
                print(f'Péen! Na verdade é {resolva}')
        print(f'Você acertou {contador2} vezes!')
        if int(contador3) == 10:
            acerteitudo.play()
            print(emoji.emojize(':1st_place_medal: Parabéns, você acertou TODAS!!:partying_face: :party_popper:'))
            sleep(2)
        elif int(contador3) < 10 and int(contador2) > 5:
            print(emoji.emojize(':2nd_place_medal: Você acertou quase tudo! Continue praticando!!'))
        elif int(contador3) == 0:
            erreitudo.play()
            print(emoji.emojize('Uau, você conseguiu errar tudo! Tô impressionade--:frowning_face:'))
            sleep(2)
        else:
            print(emoji.emojize(':3rd_place_medal: Dá pra ver que multiplicação não é seu forte, mas não desista!'))
    
    repeticao = input('Quer jogar de novo?')
    while repeticao[0].capitalize() != 'S' and repeticao[0].capitalize() != 'N':
        repeticao = input(emoji.emojize('Não entendi :thinking_face:'))
    if repeticao[0].capitalize() == 'N':
        interface.play
        print(emoji.emojize('Mas já? :sad_but_relieved_face:\nObrigade por jogar comigo! \nAté mais...:waving_hand:'))
        sleep(3)
        break
