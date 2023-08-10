# mostrar exceção ao digitar numeros negativos

num = float (input ('Digite um numero positivo: '))
if num<0:
    raise ValueError ("numero invalido")
else:
    print ("numero valido",(num))


