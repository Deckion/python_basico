# operadores lógicos
valor1= 500
valor2= 1000
valor3= 1250
# operador lógico e(AND) todas tem q ser true senao da false
print ('Verificação do valor1:', valor1<valor2 and valor1<valor3)
print ('Verificação do valor2:', valor2>valor1 and valor2>valor3)
print ('Verificação do valor3:', valor3>valor1 and valor3>valor2)
# operador lógico ou(OR) uma das duas condicoes tem q ser true 
print ('Verificação do valor1:', valor1>valor2 or valor1>valor3)
print ('Verificação do valor2:', valor2>valor1 or valor2>valor3)
print ('Verificação do valor3:', valor3>valor1 or valor3>valor2)
# operador lógico não (NOT) inverte a situaçao ou resultado
print ('Verificação do valor3:', not (valor3>valor1 or valor3>valor2))