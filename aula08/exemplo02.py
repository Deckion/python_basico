
# Funções com retorno

def soma(n1,n2): # atribuir sempre os parametros
    total = n1+n2      # variavel total so existe dentro da funcao soma 
    return total     
# print (soma (10,20))

# mostrar o dobro do resultado da função
n1 = soma (100,300)
# print (n1*2) 

# funcao para calcular a media de 3 valores

def media(n1,n2,n3):
    soma = n1+n2+n3
    return (soma)/3
# print (media (2,4,6))    

def media_tres(n1,n2,n3):
    return(n1+n2+n3)/3
# print (media (2,4,6))  

# funcao para mostrar o maior valor a partir de dois numeros

def valor(n1,n2):
    return max (n1,n2)
# print (valor (1,90))

def mostrar_maior(n1,n2):
    if n1>n2:
        return n1
    else:
        return n2
# print (mostrar_maior(1,90))


