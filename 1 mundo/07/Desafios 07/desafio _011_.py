l=float(input('Largura.?(m): '))
c=float(input('Altura.?(m): '))
t=float(input('cada litro de tinta pinta.?(m²): '))
a=l*c
print('')
print('Area:\033[33m{:.4}m²\033[m'.format(a))
print('')
r=a/t
print('para pintar uma parede de \033[33m{}m²\033[m5 precisamos de \033[34m{:.3}L de tinta'.format(a,r))
