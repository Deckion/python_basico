# estruturas de decisão(condicionais)
'''Leia a idade do aluno e defina sua categoria de acordo com as seguintes informações
Categoria - idade
Sem categoria - menor do que 3
Infantil - 3 até 10
Juvenil - 11 até 17
Adulto - 18 até 39
Senior - 40 até 130
Acima de 130 idade inválida
'''
idade = int(input('informe a idade do aluno:'))

if idade<3:
    print('aluno sem categoria definida')
elif idade <=10:
    print ('aluno da categoria infantil')
elif idade <=17:
    print ('aluno da categoria juvenil')
elif idade <=39:
    print ('aluno da categoria adulto')
elif idade <=130:
    print ('aluno da categoria senior')
else:
    print ('idade invalida')
