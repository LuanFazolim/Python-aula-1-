f=input('digite uma frase: ')


#'a'
a=f.lower().count('a')

#comeco
c=f.find('a')
co=c+1
#fim
fi=f.rfind('a')
fim=fi+1


print('Na frase \033[34m{}\033[m'.format(f))
print('')
print("Temos \033[34m{} 'a'\033[m na frase".format(a))
print('')
print('o primeiro esta na \033[32m{}\033[m posisao'.format(co))
print('')
print('e o ultimo na \033[33m{}\033[m poisao'.format(fim))