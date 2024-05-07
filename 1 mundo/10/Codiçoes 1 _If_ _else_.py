tempo=int(input('quantos anos em seu carro: '))


#Normal
print('Normal:')
print()
#-----------------------------------------------------

print("if tempo <=3:\n    print('Carro Novo')\nelse:\n    print('Carro Velho')")

print('=')

if tempo <=3:
    print('Carro Novo')
else:
    print('Carro Velho')
#----------------------------------------------------------
print('----------------------------------------------------')
print()

#Simplificada
print('Simplifiada:')
print()
#-----------------------------------------------------

print("print('Carro Novo' if tempo <=3 else 'Carro Velho')")

print('=')

print('Carro Novo' if tempo <=3 else 'Carro Velho')

#-------------------------------------------------------------------------------------------------------------------------------1
print('---------------------------------------------------------------------------------------------------------------------------')
print()
# condicional simples

print("condicional simples:")
print()
#'=='
nome=str(input('Seu nome: '))

if nome == 'gustavo':
    print('Que nome lindo voce tem!')
print('Bom dia {}!'.format(nome))


#----------------------------------------------------------
print('----------------------------------------------------')
print()
# condicional composto

print("condicional composto:")
print()
#'=='

if nome == 'gustavo':
    print('Que nome lindo voce tem!')
else:
    print('Seu nome e tao normal!')
print('Bom dia {}!'.format(nome))


#-------------------------------------------------------------------------------------------------------------------------------1
print('---------------------------------------------------------------------------------------------------------------------------')
print()
# problema classico 'media bimestral'

print("passou de ano?:")
print()

#nota
n1=float(input('nota 1: '))
n2=float(input('nota 2: '))
m=(n1+n2)/2
print('sua media foi: {:.1f}'.format(m))
if m >=6:
    print('Parabens, Media boa!!')  
else:
    print('Media Ruim')