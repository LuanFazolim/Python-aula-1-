
#jeito que fiz
from random import choice
a=(0,1,2,3,4,5)
c=choice(a)

e=int(input('Escolha um numero inteiro de \033[33m0\033[m a \033[34m5\033[m: '))

if e ==c:
    print('\033[32mVenceu!!\033[m')
else:
    print("\033[31mperdeu\033[m, o numero era \033[33m'{}'\033[m".format(c))

print()
#---------------------------------------------------------------------------
#jeito bom

print('\033[37m-'*1000)


from random import randint
from time import sleep



computador= randint(0,5)

print('\033[35m-=-'*20)

print('\033[36mVou pensar em um numero...')

print('\033[35m-=-\033[m'*20)

jogador=int(input('Em que numero pensei? '))

print('\033[37mPROCESSANDO...')
sleep(3)

if jogador ==computador:
    print('\033[32mVenceu!!\033[m')
else:
    print("\033[31mperdeu\033[m, o numero era \033[33m'{}'".format(c))


