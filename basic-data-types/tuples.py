# Nested Lists

"""
entregan el entero en n 
la seugnda linea contiene n enteros separados por espacios describiendo los elementos de la tupla. 


if __name__ == '__main__':
    n = input().split()
    t = tuple(list(input().split()))
    print(hash(t))

cree lo anterior pero no obtuve el otuput. porque no cambie los valores, recordar siempre entran
como string

"""

# no aparece nada en el codigo entonces empiezo a hacer lo mismo
if __name__ == '__main__':
    n = int(input())
    t = map(int, input().split())
    tupla = tuple(t)
    print(hash(tupla))