# ler dois numeros e executar a divisao dos valores
# try:
#     n1 = float (input("digite numerador: "))
#     n2 = float (input ("digite o denominador: "))
#     print (f"o resultado da divisão e: {n1/n2:.2f}")
# except ValueError: 
#     print('O valor informado esta incorreto!!')    
# except ZeroDivisionError:                                             #pode adicionar o nome do erro no tratamento para expecificar o erro
#     print ('Houve um problema ao executar a operação, tente novamente..')

# oooooouuuuu

try:
    n1 = float (input("digite numerador: "))
    n2 = float (input ("digite o denominador: "))
    print (f"o resultado da divisão e: {n1/n2:.2f}")
except:
    print ('Não foi possivel completar a operação')

