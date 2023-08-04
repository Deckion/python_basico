valor1=45
valor2=258.45

# operadores aritméticos
print('soma:',                         valor1+valor2)
print('subtração:',                    valor1-valor2)
print('multiplicação:',                valor1*valor2)
print('divisão:',                      valor1/valor2)
print(f'divisão com 2 casas decimais: {valor1/valor2:.2f}')
print(f'valor 2: {valor2:.1f}')
# obter dados do teclado (entrada de dados)
usuario = input('Informe o seu nome:')
print(f"Seja bem-vindo(a) {usuario}")
# conversão de tipo de dados - Casting (str para int)
idade = int (input("informe sua idade:"))
print(f'O nome do usuario é {usuario} e sua idade informada é {idade} ')
# mostrar o dobro da idade informada pelo usuario
print(f'o dobro da idade do usuario é {idade*2}' )
# mostrar tipos de dados das variaveis
print('idade:', type (idade))
print('usuario:',type(usuario))
# valor do curso vai ser float por ter numeros com virgula
valor_curso = float (input('informe o valor pago pelo curso:'))
print (f'O valor informado foi {valor_curso}')
# mostrar uma msg com 25% do valor do curso
# Parabéns! vc ganhou <valor> de credito na proxima compra
print (f'Parabéns! vc ganhou o 25% de credito na proxima compra {valor_curso/4}')
#solicitar quantidade de parcelas do pagamento
parcela = int(input ('Informe quantidade de parcelas:'))
# mostrar valor das parcelas sem juros
print (f' Valor das parcelas sem juros será de R$ {valor_curso/parcela}')
