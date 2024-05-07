s=float(input('Salario: '))
a=float(input('\033[32mAumento(\033[35m%\033[32m)\033[m: '))
print('')
p=a/100*s
r=p+s
print('com o aumento voce ganhara \033[32m{} R$'.format(r))
