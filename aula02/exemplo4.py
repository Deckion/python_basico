# leia dois numeros inteiros e mostre somente o menor valor
print ("Informe numeros inteiros abaixo:")

num1 = int (input("Primeiro número: "))
num2 = int (input("Segundo número: "))


if num1<num2:
    print ("Menor número inteiro:", num1)
elif num1==num2:
    print("Os números sao iguais, tente novamente.")    
else:
    print ("Menor número inteiro:", num2)
print("fim")