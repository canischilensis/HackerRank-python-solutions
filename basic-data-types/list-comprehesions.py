if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

"""
- Cuboide: caja con forma de paralelepípedo.
- x, y, z: tamaño de la caja (largo, fondo, alto). Son fijos.
- i, j, k: coordenadas de un punto. Van cambiando.
- Grilla: todos los puntos con coordenadas enteras dentro de la caja.
    - Ej.: x=2, y=1, z=1 -> 12 puntos (8 esquinas + 4 intermedios).
- Regla 1: recorrer la grilla -> i de 0 a x, j de 0 a y, k de 0 a z.
- Regla 2: descartar los puntos donde i + j + k == n.
    - Ej.: [2, 0, 0] con n=2 -> 2+0+0 = 2 -> se descarta.
"""
#Declaro una lista vacia para que se guarde la grilla
    grid = []

# con bucles para entender la logica 
# tomo ideas desde el desafio print-funciont.py, le agrego un +1 al parametro dentro de la funcion range
# empiezo con el eje x
    for i in range(0,x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k != n:
                    grid.append([i,j,k])

# como seria en una list comprehensions 
    grid = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if ((i+j+k) != n)]