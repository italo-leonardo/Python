positivo = 0
total = 0

for num in range(1, 7):
    num = float(input())
    if num >= 0:
        positivo += 1
        total += num
        
media = total / positivo

print(f'{positivo} valores positivos')
print(f'{media}:.1f')