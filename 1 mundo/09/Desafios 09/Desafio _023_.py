numero=(input('Esreva um numero de no maximo 4 digitos: '))
l=len(numero)

#unidade
m2=l-1
u=numero[m2::]

#dezena
m3=l-2
d=numero[m3:m2:]

#centena
m4=l-3
c=numero[m4:m3:]

#Milhar

m5=l-4
mi=numero[m5:1:]



print('   \033[35mMilhar\033[m   |   \033[34mCentena\033[m   |   \033[33mDezena\033[m   |   \033[32mUnidade\033[m  ')
print('      {}           {}             {}            {}      '.format(mi,c,d,u))
