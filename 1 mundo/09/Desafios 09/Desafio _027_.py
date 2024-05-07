nome=input('Seu nome completo: ')
qua=nome.split()
l=len(qua)
s=l-1
nm=qua[0]
nma=qua[s]
n1=nm.capitalize()
n2=nma.capitalize()

print('\033[32m{} \033[31m{}'.format(n1,n2))