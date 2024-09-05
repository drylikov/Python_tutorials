"""
    Implementacion del algoritmo llamado
    Quicksort o de ordenamiento rapido
    sobre una lista y que retorna una lista 
    ordenada. Algoritmo elemental.

"""

def sort_quick(seq):

    if len(seq) < 1:
        return seq
    else:
        pivot = seq[0]
        seq1 = sort([x for x in seq[1:] if x < pivot])
        seq2 = sort([x for x in seq[1:] if x >= pivot])
        return seq1 + [pivot] + right
