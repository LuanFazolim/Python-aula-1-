palavra = str(input('\033[42mPalavra\033[m:'))

if palavra == '':
    palavra = (' ')

# ------------------------------------------------------------------------------------------------------------------------
# letra
letra1 = str(input('\033[;41mLetra:\033[m'))

letra = letra1.lower()
if letra == 'normal' or letra == 'norm':
    letra1 = ('0')

if letra == 'padrao' or letra == 'padra' or letra == 'padr' or letra == 'pad':
    letra1 = ('1')

if letra == 'negrito' or letra == 'neg' or letra == 'negrita':
    letra1 = ('4')

if letra == 'negativo' or letra == 'oposto' or letra == 'nega' or letra == 'opo' or letra == 'negativa':
    letra1 = ('7')

# ------------------------------------------------------------------------------------------------------------------------

# cor
cor1 = str(input('\033[;44mCor:\033[m'))

cor = cor1.lower()

if cor == 'preto' or cor == 'pret' or cor == 'pre' or cor == 'vermel' or cor == 'pr' or cor == 'black':
    cor1 = (';30')

if cor == 'vermelho' or cor == 'vermelha' or cor == 'vermelh' or cor == 'vermel' or cor == 'verme' or cor == 'verm' or cor == 'red':
    cor1 = (';31')

if cor == 'verde' or cor == 'verd' or cor == 'greem':
    cor1 = (';32')

if cor == 'amarelo' or cor == 'amarela' or cor == 'amare' or cor == 'ama' or cor == 'yellow':
    cor1 = (';33')

if cor == 'azul' or cor == 'azu' or cor == 'az' or cor == 'blue':
    cor1 = (';34')

if cor == 'roxo' or cor == 'rox' or cor == 'ro' or cor == 'purple':
    cor1 = (';35')

if cor == 'azul bebe' or cor == 'azul b' or cor == 'azb' or cor == 'baby blue':
    cor1 = (';36')

if cor == 'cinza' or cor == 'cinz' or cor == 'cin' or cor == 'gray':
    cor1 = (';37')

# --------------------------------------------------------------------------------------------------------------------------


# Fundo
fundo1 = str(input('\033[;45mFundo:\033[m'))

fundo = fundo1.lower()

if fundo == 'preto' or fundo == 'pret' or fundo == 'pre' or fundo == 'vermel' or fundo == 'pr' or fundo == 'black':
    fundo1 = (';40')

if fundo == 'vermelho' or fundo == 'vermelha' or fundo == 'vermelh' or fundo == 'vermel' or fundo == 'verme' or fundo == 'verm' or cor == 'red':
    fundo1 = (';41')

if fundo == 'verde' or fundo == 'verd' or fundo == 'greem':
    fundo1 = (';42')

if fundo == 'amarelo' or fundo == 'amarela' or fundo == 'amare' or fundo == 'ama' or cor == 'yellow':
    fundo1 = (';43')

if fundo == 'azul' or fundo == 'azu' or fundo == 'az' or fundo == 'blue':
    fundo1 = (';44')

if fundo == 'roxo' or fundo == 'rox' or fundo == 'ro' or fundo == 'purple':
    fundo1 = (';45')

if fundo == 'azul bebe' or fundo == 'azul b' or fundo == 'azb' or fundo == 'baby blue':
    fundo1 = (';46')

if fundo == 'cinza' or fundo == 'cinz' or fundo == 'cin' or fundo == 'gray':
    fundo1 = (';47')

print()
# ------------------------------------------------------------------------------------------------------------

# fim
t = ('\ 0 ')
f = t[::2]
fim = ('\033[;33m{}33[m'.format(f))

i = '\033[{}{}{}m'.format(letra1, cor1, fundo1)
print(i + palavra + '\033[m')