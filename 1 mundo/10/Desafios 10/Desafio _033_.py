n1=int(input('n1: '))
n2=int(input('n2: '))
n3=int(input('n3: '))


#maior
if n1 >=n2:
    if n1 >=n3: print('{} E o \033[34mmaior\033[m'.format(n1))
if n2 >=n1:
    if n2 >=n3: print('{} E o \033[34mmaior\033[m'.format(n2))
if n3 >=n2:
    if n3 >=n1: print('{} E o \033[34mmaior\033[m'.format(n3))

#menor
if n1 <=n2:
    if n1 <=n3: print('{} E o \033[31mmenor\033[m'.format(n1))
if n2 <=n1:
    if n2 <=n3: print('{} E o\033[31m menor\033[m'.format(n2))
if n3 <=n2:
    if n3 <=n1: print('{} E o \033[31mmenor\033[m'.format(n3))