#Criando programa que peça
#Nome, cargo, salario atual e % do aumento
#e mostre os dados com salario antigo e salario novo
nome = str(input('Digite seu nome!'))
cargo = str(input('Qual seu Cargo?'))
aumento = float(input('Quanto de aumento voce quer?'))
salario = float(input('Qual seu salario?'))
nsalario = salario*aumento/100 + salario
print(f'''Nome: {nome}\nCargo: {cargo}
Salario: R${salario:.2f}\nAumento: {aumento}%\nSeu novo salário com aumento é R${nsalario:.2f}''')