#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
computador = randint(0, 10)
print('-='*20)
print('\033[37mJOGO DE ADIVINHAÇÃO V2.0\033[m')
print('-='*20)
print('''Olá, sou o \033[33mAutodax\033[m...
Acabei de pensar em um número entre 0 e 10.
\033[36mVocê consegue adivinhar\033[m?''')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('\033[34mMais...Tente novamente!\033[m')
        elif jogador > computador:
            print('\033[34mMenos...Tente novamente!\033[m')
print('\033[32mAcertou mizeravi! Você teve \033[1;32m{}\033[m \033[32mtentativas. Parabéns!\033[m'.format(palpites))

