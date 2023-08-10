
try:
    print (x)
except Exception as e: #mostra qual o erro, mas nao mostra o nome do erro
    print ('Falha ao acerrar a variável')
    print (e)
else:
    print ("Parabéns! funfou!")
finally:
    print ("Fim do tratamento de exceções")





