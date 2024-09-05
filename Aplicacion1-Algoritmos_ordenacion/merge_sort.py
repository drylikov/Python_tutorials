"""Implementacion del algoritmo merge 
    sobre una lista y retorna una lista 
    ordenada.

    Se usa  la tecnica divide and conquer recursivamente para 
    dividir y ordenar la lista

"""

def merge(seq1, seq2):
    resultado = []
    n ,m = 0, 0
    while n < len(seq1) and m < len(seq2):
        if seq1[n] <= seq2[m]:
            resultado.append(seq1[n])
            n += 1
        else:
            resultado.append(seq2[m])
            m += 1

    resultado += seq1[n:]
    resultado += seq2[m:]
    return resultado

def sort(seq):
    if len(seq) <= 1:
        return seq
    
    media = len(seq) /2
    seq1 = sort(seq[:media])
    seq2 = sort(seq[media:])
    return merge(seq1, seq2)

       
