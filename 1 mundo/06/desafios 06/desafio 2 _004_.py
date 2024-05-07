q=input('digite algo:')
print(type(q))

le=q.isalpha()
ap=q.isalnum()
lma=q.isupper()
lmi=q.islower()
nu=q.isnumeric()
es=q.isspace()
ca=q.istitle()

print('\033[;32me uma letra?:',le)
print('\033[;36me um alphanumerico?:',ap)
print('\033[;33me uma letra maiuscula?:',lma)
print('\033[;31me uma letra minuscula?:',lmi)
print('\033[;32me um numero?:',nu)
print('\033[;34mso tem espacos?:',es)
print('\033[;35mesta capitalizada?',ca)

