import math
def trigonometry(a):
    ra = math.radians(a)
    sin = math.sin(ra)
    cos = math.cos(ra)
    tan = math.tan(ra)
    return sin,cos,tan
a=float(input('Angulo: '))
sin, cos, tan = trigonometry(a)
print('\033[34mSeno = {:.2f}'.format(sin))
print('\033[35mCosseno = {:.2f}'.format(cos))
print('\033[33mTangente = {:.2f}'.format(tan))


