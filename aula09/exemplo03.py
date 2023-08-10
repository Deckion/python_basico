# ler a idade de um funcionario e tratar possiveis numeros negativos ou valores acima de  130


idade = int (input ("digite a idade do funcionario: "))
if idade<=0 or idade>=130:
    raise Exception ('idade invalida')
else:
    print ("A idade do funcionario é valida ")








