media = int(input())

match media:
    case media if media < 5:
        print("Voce foi reprovado")
    case media if 5 <= media < 7:
        print("Voce fara a recuperacao")
    case media if media >= 7:
        print("Voce foi aprovado")