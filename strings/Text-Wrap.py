"""
stirng S con largo w 
hay que envolver (wrap) en un parrafo de ancho w 

sde me entregan una cadena y debo partir cuantas las veces segun el largo 
el largo es un numero que entregan en la segunda linea
al parecer debo hacer una lista con cada pedazo usando un silicing
naa era una libreria nada que ver era mas faicl ! 

"""

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string,max_width)
    

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)