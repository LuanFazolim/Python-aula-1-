from random import choice
n1=input('aluno 1:')
n2=input('aluno 2:')
n3=input('aluno 3:')
n4=input('aluno 4:')
r=n1,n2,n3,n4
c=choice(r)
print('\033[31m{}\033[m apaga a lousa!!'.format(c))
