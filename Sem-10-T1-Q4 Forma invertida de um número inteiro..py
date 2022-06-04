def inverter_nu(n):
    inverter = 0
    while n > 0:
        inverter = (inverter * 10) + n % 10
        n = n // 10
    return inverter

n = int(input())
inverter = inverter_nu(n)
print(inverter)
