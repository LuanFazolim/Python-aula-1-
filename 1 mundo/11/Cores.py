print("coloque","'\033[33m\+""033['numero' m\033[m' e no final","'\033[33m\+""033[m\033[m'")

print('\033[37mstyle                  text     bach')

#Anotaçao  '30 ao 33' '40 ao 43'
print('\033[33m0\033[m = none                \033[30m30\033[m       \033[40m40\033[m\n\033[33m1\033[m = bold                \033[31m31\033[m       \033[41m41\033[m\n\033[4;33m4\033[m = underline           \033[32m32\033[m       \033[42m42\033[m\n\033[7;33m7\033[m = negative            \033[33m33\033[m       \033[43m43\033[m')
#'34 ao 37' '44 ao 47'
print('                        \033[34m34\033[m       \033[44m44\033[m\n                        \033[35m35\033[m       \033[45m45\033[m\n                        \033[36m36\033[m       \033[46m46\033[m\n                        \033[37m37\033[m       \033[47m47\033[m')


#exemplos
print()

print('Exemplos:')
print('\033[32mOla, vc e bom!!\033[m')

print('Ola, vc e \033[31mruim!!\033[m')

print('\033[31ma\033[32mr\033[33mc\033[34mo\033[37m-\033[35mi\033[36mr\033[31mi\033[33ms')

print('\033[4;37mnegrito')

print('\033[0;31;44mHomem-Aranha\033[m')

print('\033[40mCorinthians\033[m')

#ou

print('Vc tirou {}{}{} na prova!!'.format('\033[31m','5','\033[m'))

print('Vc tirou {}{}{} na prova!!'.format('\033[32m','10','\033[m'))

#resumir
print()
print('Resumir:')
cores={'vermelho':'\033[31m',
       'verde':'\033[32m',
       'azul':'\033[34m',
       'fim':'\033[m'}

print('Assim fica bem mais facil, {}azul{}, {}verde{}, {}vermelho{}'.format(cores['azul'],cores['fim'],cores['verde'],cores['fim'],cores['vermelho'],cores['fim']))


