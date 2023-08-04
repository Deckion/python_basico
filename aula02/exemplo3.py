# Leia a idade do usuário e informe se ele é maior ou menor de idade
# Verificar numeros negativos antes da idade
print ('Usuário por favor informe sua idade:')

idade = int (input ("Sua idade aqui: "))

if idade>18:
    print("Usuário é maior de idade.")
elif idade<=0:
    print("idade invalida")
else:
        print ("O usuário é menor de idade.")
print ("fim")


