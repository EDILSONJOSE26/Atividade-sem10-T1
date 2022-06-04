mes = 10
ano = 2016

salario = float(input())
divida = float(input())

while salario > divida:    
    divida  = (divida * 0.15) + divida
    mes += 1
    if mes == 13:
        mes = 1
        ano += 1
    if mes == 3:
            salario = (salario * 0.05) + salario
print(f'{mes}/{ano}')
