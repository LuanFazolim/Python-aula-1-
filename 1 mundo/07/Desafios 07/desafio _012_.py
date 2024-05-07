v=float(input('preço: '))
d=float(input('\033[31mdesconto(\033[35m%\033[31m)\033[m: '))
p=d/100*v
m=v-p
print('com desconto fica \033[32m{}R$'.format(m))