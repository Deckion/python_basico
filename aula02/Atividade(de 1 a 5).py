"""
1.	Faça um Script em Python que apenas imprima o seu nome na tela e em seguida finalize a aplicação. 
"""
print ("Giuliano")
print ("---------Fim1-----------")

"""
2.	Faça um Script em Python que solicite ao usuário digitar o seu nome e em seguida envie a seguinte frase para a saída padrão: "O seu nome é: [nome do usuário]". 
"""
print ("Digite seu nome abaixo:")
nome = str (input("Seu nome aqui: "))
print ("Seu nome é:", nome)
print ("---------Fim2-----------")

"""
3.	Faça um Script em Python que solicite o nome e a idade do usuário e então, envie a seguinte frase para o Console: "O seu nome é <nome> e a sua idade é <idade>". 
"""
print ("Insira seu nome e idade abaixo:")
nome = str (input("Seu nome aqui: "))
idade = int (input("Sua idade aqui: "))
print ("seu nome é:", nome, "e sua idade:", idade)
print ("---------Fim3-----------")

'''
4.	Faça um Script em Python que solicite ao usuário informar um número. Em seguida, armazene este número numa variável e por fim, mostre o dobro e a metade do valor digitado. 
'''
print ("Informe numero abaixo:")
num = int (input('Digite numero: '))
print ("O dobro do numero informado é:",num*2)
print ('A metade do numero informado é:',num/2)
print ("---------Fim4-----------")

'''
5.	Faça um Script em Python que solicite ao usuário informar 3 números. Em seguida, some-os e envie para a saída padrão a seguinte frase: "A soma total é: " 
'''
print ('informe 3 numeros abaixo na sequencia:')
num1 = float (input ('digite o primeiro numero:'))
num2 = float (input ('digite o segundo numero:'))
num3 = float (input ('digite o terceito numero:'))
print ('A soma total é:',num1+num2+num3)