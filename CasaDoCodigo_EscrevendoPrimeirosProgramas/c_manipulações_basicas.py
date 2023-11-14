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

impostos = ['MEI', 'Simples']
for imposto in impostos:
    print(imposto)
    
impostos = ['MEI', 'Simples']
for x in imposto:
    print(x)

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for lista in lista:
    print(lista)

print('stop')

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in lista:
    print(i)
    
for i in range(5):
    print(i)
    
    
impostos = ['MEI', 'Simples']
for i, imposto in enumerate(impostos):
    print(i, imposto)

def sum(a, b):
    return a + b
c = sum(1, 3)
print(c)

def salario_descontado_imposto(salario, imposto=27.):
    return salario - (salario * imposto * 0.01)

res_salario = salario_descontado_imposto(1000)
print(res_salario)

from datetime import date
d = (2013, 3, 15)
print(date(d[0], d[1], d[2]))

from datetime import date
d = (2013, 3, 15)
print(date(*d))

def new_user(active=False, admin=False):
    print(active)
    print(admin)
config = {"active": False, "admin": True}
new_user(**config)

def unpacking_experiment(*args):
    arg1 = args[0]
    arg2 = args[1]
    others = args[2:]
    print(arg1)
    print(arg2)
    print(others)
unpacking_experiment(1, 2, 3, 4, 5, 6)

'''

def unpacking_experiment(**kwargs):
    print(kwargs)
unpacking_experiment(named="Test", other="Other")

def unpacking_experiment2(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

unpacking_experiment2(a=1, b=2, c=3)