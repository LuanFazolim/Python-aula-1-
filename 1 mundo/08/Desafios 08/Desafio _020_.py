
from random import shuffle
n1 = (input('aluno 1:'))
n2 = (input('aluno 2:'))
n3 = (input('aluno 3:'))
n4 = (input('aluno 4:'))
lista = ['{}, {}, {}, {}'.format(n1,n2,n3,n4)]
shuffle(lista)
print('\033[33mA ordem e:\033[32m')
print(lista)
