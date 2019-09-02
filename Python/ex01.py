'''
Calcular a média do aluno a partir de 3 notas sendo que a primeira prova tem peso 2, a segunda prova tem peso 3 e a terceira prova tem peso 5
É uma média ponderada
'''

nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
nota3 = float(input('Digite a nota 3: '))

# Declaração dos pesos
pesos = [2,3,5]
total = 0

for value in pesos:
    total += value

media = (nota1*pesos[0] + nota2*pesos[1] + nota3*pesos[2]) / (total)
print(media)