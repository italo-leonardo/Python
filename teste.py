n = input().split()

x = float(n[0])
y = float(n[1])

if x > 0 and y > 0:
    print('Q1')
elif x < 0 and y > 0:
    print('Q2')
elif x < 0 and y < 0:
    print('Q3')
elif x > 0 and y <0:
    print("Q4")
else:
    print('Origem')
    