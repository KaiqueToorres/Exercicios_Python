#Exercicio 01 - Montando um triangulo
V1=int(input('Primeiro Lado '))
V2=int(input('Segundo Lado '))
V3=int(input('Terceiro Lado '))
if (V1+V2<V3) or (V1+V3<V2) or (V2+V3<V1):
  print ('Não é um triangulo')
elif (V1==V2) and (V1==V3):
  print ('É um triangulo Equilatero')
elif (V1!=V2) and (V1!=V3) and (V2!=V3):
  print ('É um triangulo Escaleno')
else:
  print ('É um triangulo Isosceles')