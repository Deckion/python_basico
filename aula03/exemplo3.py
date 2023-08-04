# aplicar operadores lógicos com if
# leia a quantidade de faltas de um aluno e sua média final
faltas = int (input("Insira quantidade de faltas:"))
media = float (input ('Insira as media final:'))

# condicoes de reprovação:
# qnt de faltas maior que 8 OU media menor que 7
print ('*'*50)
# analisar condição do aluno somente se o valor das faltas for menor ou igual a zero
if faltas<0:
    print('faltas invalidas')
elif faltas>8 or media<7:
    print('Aluno reprovado')
else:
    print('aluno aprovado')
    
# analisar condição do aluno somente se o valor das faltas for maior ou igual a zero
if faltas>=0:    
    if faltas>8 or media<7:
       if faltas>8:
           print ('aluno reprovado por faltas') 
       if media<7:
           print ('aluno reprovado por nota')    
    else:
        print('Aluno aprovado')
else:
    print ('Valor das faltas invalido')
