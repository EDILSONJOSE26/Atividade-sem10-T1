x = 0
número = 0
while True:
    e = int(input())
    if e > 0:
        número += e
        x += 1
    else:
        break
if x > 0:
    s = número / x
    print(f'{s:.2f}')