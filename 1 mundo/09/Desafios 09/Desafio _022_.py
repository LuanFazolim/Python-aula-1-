nome=str(input('Seu nome completo: '))
t=len(nome)

#1
Ma=nome.upper()

#2
mi=nome.lower()

#3
r=nome.count(' ')
s=t-r

#4
sp=nome.split()
pr=sp[0]
le=len(pr)



print('')
print(Ma)
print('')
print(mi)
print('')
print("'{}' tem \033[32m{} \033[mletras".format(nome,s))
print('')
print("Seu primeiro nome e \033[34m'{}'\033[m e tem \033[32m'{}'\033[m letras".format(pr,le))


