'''6.	Faça um Script em Python que solicite ao usuário informar 3 números. Em seguida, multiplique os valores e envie para a saída padrão a seguinte frase: "A multiplicação entre <X>, <Y> e <Z> é igual <Total>". 
'''
print ('informe 3 numeros abaixo na sequencia:')
num1 = float (input ('digite o primeiro numero:'))
num2 = float (input ('digite o segundo numero:'))
num3 = float (input ('digite o terceiro numero:'))

print (f'A multiplicação entre ',num1,",", num2, "e", num3, "é igual a:", num1*num2*num3)
print ("---------Fim6-----------")

'''
7.	Faça um Script em Python que solicite a nota das 4 provas semestrais do usuário. Em seguida, calcule e envie para a saída padrão a média
'''
print ('informe 4 notas de provas abaixo:')
num1 = float (input ('digite o primeira nota:'))
num2 = float (input ('digite o segunda nota:'))
num3 = float (input ('digite o terceira nota:'))
num4 = float (input ('digite o quarta nota:'))

print ('média das notas:',(num1+num2+num3+num4)/4)
print ("---------Fim7-----------")

'''
8.	Faça um Script em Python em que o usuário informe uma medida em metros. Em seguida, converta essa medida para centímetros e envie para a saída padrão: 
'''
metros = int (input ("informe medida em metros:"))
print ('medida em centimetros é:',metros*100)
print ("---------Fim8-----------")

'''9.	Faça um Script em Python que calcule o cubo e o quadrado de um determinado número
'''
num = int (input ('informe número:'))
print ('O cubo do número é:',num**3)
print ('O quadrado do número é:',num**2)
print ("---------Fim9-----------")