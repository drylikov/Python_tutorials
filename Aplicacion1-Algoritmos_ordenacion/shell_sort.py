"""El ordenamiento shell, un algoritmo de
    ordenamiento.
    Implementacion del ordenamiento shell en
    una lista y retorna una lista ordenada
    en Python

"""

def shell(seq):
    L = [x for x in range(len(seq)/2,0,-1)]
    for l in L:
        for i in range(l, len(seq)):
            temp = seq[i]
            j = i
            while j> l and seq[j-l] > temp:
                seq[j] = seq[j -l]
                j -= l
                seq[j] = temp

    return seq
