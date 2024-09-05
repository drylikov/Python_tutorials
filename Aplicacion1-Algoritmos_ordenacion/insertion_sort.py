"""Implementacion por insercion sobre una
    lista y retorna una lista ordenada
    Algoritmo Elemental
    """

def sort(seq):
    for n in range(1, len(seq)):
        item = seq[n]
        ins = n
        while ins > 0 and seq[ins -1] > item:
            seq[ins] = seq[ins-1]
            ins = ins -1
        seq[ins] = item
    return seq
