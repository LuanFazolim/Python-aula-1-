d=int(input('Distancia da viagem Km: '))

if d <=200:
    print('{:.2f} \033[32mR$\033[m'.format(0.50*d))
else:
    print('{:.2f}\033[32mR$\033[m'.format(0.45*d))