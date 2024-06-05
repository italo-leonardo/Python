n = int(input())
total = n
ced = 100
totcad = 0
while True:
    if total >= ced:
        total -= ced
        totcad += 1
    else:
        print(f'{totcad} nota (s) de R${ced:.2f}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced == 2
        elif ced == 2:
            ced == 1
        totcad = 0
        if total == 0:
            break