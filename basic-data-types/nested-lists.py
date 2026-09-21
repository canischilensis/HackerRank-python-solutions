# Nested Lists

"""
entregan el entero en n 
la seugnda linea contiene n enteros separados por espacios describiendo los elementos de la tupla. 

"""

# no aparece nada en el codigo entonces empiezo a hacer lo mismo
if __name__ == '__main__':
    n = input().split()
    t = tuple(list(input().split()))
    print(hash(t))