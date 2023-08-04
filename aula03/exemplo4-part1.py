# estrutura de repetição WHILE (enquanto)

cont = 0
while cont<=10:
    print (cont, end=" ")
    cont = cont+1
print ('\nvalor final do contador', cont)     

# contagem iniciando em 50 ate 200

cont = 50
while cont<=200:
    print (cont, end=" ")
    cont +=1
print ('-'*50)

# contagem iniciando em 10 e finalizando em 80, incrementando os valores de 10 em 10

cont = 10
while cont<=80:
    print (cont, end=" ")
    cont +=10
print ('\n','-'*70)

# mostrar a msnsagem "eu tenho que estudar" 300x
cont = 1
while cont<=300:
    print (cont,"eu tenho que estudar")
    cont +=1
print ('-'*50)
# leia um numero e mostre a contagem a partir de zero ate o numero informado

num = int (input ('Insira numero:'))
cont = 0 
while cont <=num:
    print (cont, end=" ")
    cont +=1
print ('\n','😁'*10)

# contagem decrescente iniciando em 23 ate 0

cont = 23 
while cont >=0:
    print (cont, end=" ")
    cont -=1
print ('\n','-'*70)

# leia 2 numeros e mostre a contagem do intervalo dos valores informados
num1 = int (input ('Insira primeiro crescente numero:'))
num2 = int (input ('Insira segundo crescente numero:'))


while num1<=num2:
    print (num1, end=" ")
    num1+=1
    

