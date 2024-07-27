while True:
    num = int(input("Quar ver a tabuada de qual valor? "))
    if num < 0:
        print("PROGRMA TABUADA ENCERRADO. Volte sempre!")
        break
    else:
        for t in range(1, 11): 
            print(f"{num} x {t} = {num*t}")
            t += 1
        
