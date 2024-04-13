s = 0
for c in range(1, 500 , 2): # Numero imparres
    if c % 3 == 0: # Calculo para saber se é multiplo de 3
        s += c # Soma de todos os multiplos de 3 
print('A soma de todos os numeros impares de 1 a 500 que são multiplo de 3: {}'.format(s))