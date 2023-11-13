''' 
salario = int(input('Digite o salario: '))
imposto = float(input('Digite o Imposto em % (ex: 27.5)? '))
print("O salario Liquido é: {0}".format(salario - (salario *(imposto * 0.01))))

print(1 >= 1)
print(2 < 1)
print(9 == 9)
print(9 != 8)
print(2 <= 3)

salario = int(input('Salario? '))
imposto = input('Imposto em % (ex: 27.5)? ')

if imposto == '':
    imposto = 27.5
else:
    imposto = float(imposto)
    
print("Valor real: {0}".format(salario - (salario *(imposto * 0.01))))


imposto = float(input("Imposto: "))
if imposto < 10:
    print("Medio")
elif imposto < 27.5:
    print("Alto")
else:
    print("Muito alto")
    
salario = int(input('Salario? '))
imposto = 27.0  # Inicializa como um número de ponto flutuante

while True:
    imposto = input('Imposto ou (0) para sair: ')

    if not imposto:
        imposto = 27.0
    else:
        imposto = float(imposto)
    if imposto == 0:
        break

'''

impostos = ['MEI', 'Simples']
for imposto in impostos:
    print(imposto)
    
impostos = ['MEI', 'Simples']
for x in imposto:
    print(x)

