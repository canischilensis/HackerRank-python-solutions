"""
se puede cortar un string ubicando las posiciones que 
corresponden: 
string = string[:5] + "k" + string[6:]
se agrega k en esa posicion. 
---
pirmera linea contiene la cadena string
la sigueinte linea contiene la posicion, el indice y la cadena. 
"""

def mutate_string(string, position, character): 
    return string[:position]+character+string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

"""
STDIN           Function
-----           --------
abracadabra     s = 'abracadabra'
5 k             position = 5, character = 'k'
"""