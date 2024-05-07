print('    Ola Amigo, Voce Me Ouve    ')
print('')
print('-----------------------------------------------------------')
#indentificar se tem ou nao na frase
frase=('    Ola Amigo, Voce Me Ouve    ')
t='Ola'in frase
f='colega'in frase
print('ola:',t)
print('colega:',f)

print('-----------------------------------------------------------')

#indentificar numeros de espacos da frase
espacos=len(frase)
print('A frase oculpa {} espacos'.format(espacos))

print('-----------------------------------------------------------')

#fatiamento
fatiamento1=frase[::1]
fatiamento2=frase[5::1]
fatiamento3=frase[:17:1]
fatiamento4=frase[::3]
print('fatiamento 1:  ',fatiamento1)
print('fatiamento 2:  ',fatiamento2)
print('fatiamento 3:  ',fatiamento3)
print('fatiamento 4:  ',fatiamento4)

print('-----------------------------------------------------------')

#transformacao
transformacao=frase.replace('Amigo','cara')
print(transformacao)

print('-----------------------------------------------------------')

#Miuscula e Minuscula e etc
Maiuscula=frase.upper()
Minuscula=frase.lower()
Primeira=frase.capitalize()
Palavras=frase.title()
print("'{}' =    '{}'".format(frase,Maiuscula))
print("'{}' =    '{}'".format(Maiuscula,Minuscula))
print("'{}' =    '{}'".format(Minuscula,Primeira))
print("'{}' =    '{}'".format(Primeira,Palavras))

print('-----------------------------------------------------------')

#Espaos inuteis
inutil=frase.strip()
inutilr=frase.rstrip()
inutill=frase.lstrip()
print('{}'.format(inutil))
print('{}'.format(inutilr))
print('{}'.format(inutill))

print('-----------------------------------------------------------')

#Divisao e juncao de espacos
divisao=frase.split()
juncao=''.join(frase)
juncao2='-'.join(frase)
print(divisao)
print(juncao)
print(juncao2)

print('-----------------------------------------------------------')

#contagem de letra
o=frase.lower().count('o')
a=frase.lower().count('a')
m=frase.lower().count('m')

print("Na frase '{}'\nTemos: {} 'o'\nTemos: {} 'a'\nTemos: {} 'm'".format(frase,o,a,m))


print('-----------------------------------------------------------')

#Divisao da frase 2
divisao2=frase.split()
letra=divisao2[2][3]
print("A 2 palavra da frase e: '{}'\nE sua 3 letra e: '{}'".format(divisao2[2],letra))

print('-----------------------------------------------------------')


