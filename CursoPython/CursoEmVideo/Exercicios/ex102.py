def fat(num, show=False):
    """
    -> Calcula o Fatorial de um número:
    :param n: o Fatorial a ser calculado
    :parem show: (opcional) Mostrar ou não o conta
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for i in range(num, 0, -1):
        if show:
            print(i, end="")
            if i > 1:
                print(' x ', end="")
            else:
                print(' = ', end="")
        f*= i
    return f

print(fat(5))
#help(fat)