carro=int(input('Km: '))

if carro >80:
    print('Voce foi \033[31mmultado!!\033[m, a Multa sera de \033[32m{} R$'.format((carro-80)*7))
else:
    print('\033[32mTenha um bom dia! Dirija com segurança!')