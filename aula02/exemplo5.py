# leia o valor de um produto, caso o valor seja menor do que 100 mostre a seguinte mensagem
# "Você recebeu 5% de desconto", caso contrário "Você recebeu 10% de desconto"

print ("Informe valor do produto abaixo:")

produto = float (input ("Informe valor:"))

if produto<100:
    print ("Você recebeu 5% de desconto")
else:
    print ("Você recebeu 10% de desconto")
print ("fim")

