# Estudo de um programa de adivinhação. Você tenta adivinhar um número que o computador "pensou".
# Study of a divination program. You try to guess a number that the computer "thought".

from random import randint
from time import sleep
from emoji import emoji_lis
computador = randint(0, 10)          # Faz o computador "pensar" em um número
print('\033[0;0;33m-=-\033[m'*20)
print('Vou pensar em um número de 0 à 10 e você vai tentar adivinhar')
print('\033[0;0;33m-=-\033[m'*20)
jogador = int(input('\033[0;0;34mEm que número eu pensei?\033[m '))     # Jogador tenta adivinhar
print('\033[0;0;31mPROCESSANDO...\033[m')
sleep(1)
if jogador == computador:
      print('\033[0;0;35mPARABÉNS!:boom:\033[m Você conseguiu me vencer!')
else:
      print('\033[0;0;36mGANHEI!:v:\033[m Eu pensei no número \033[1;0;37m{}\033[m e não no {}!'.format(computador, jogador))
print('\033[0;0;33m-=-\033[m'*20)

