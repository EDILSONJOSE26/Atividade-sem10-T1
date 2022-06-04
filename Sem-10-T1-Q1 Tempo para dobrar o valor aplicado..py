deposito = float(input())
juros = float(input())
quantidade = 0
objetivo = 2 * deposito
montante = 0
while montante < objetivo:        
    montante = (deposito * (juros/100)) + deposito
    deposito = montante
    quantidade += 1        

print(f'{quantidade}')
