
"""
#lists hackerrank
if __name__ == '__main__':
    N = int(input())
    lista = []
    for _ in range(N):
        # El asterisco en *d reparte: la primera palabra va a s y todo el resto se junta en d, que siempre queda como lista aunque esté vacía.
        s, *d = input().split()
        # d se queda con los numeros y ahora se deben convertir a enteros
        d = list(map(int,d))
        if s == "print":
            print(lista)
        else:
            # getattr() obtiene un atributo de un objeto usando su nombre como texto
            # primer parametro es la lista a cambiar y el segundo parametro es el metodo. 
            getattr(lista, s)(*d)
"""

if __name__ == '__main__':
    N = int(input())
    L = []
    for _ in range(N):
        A = list(input().split())
        cmd = A[0] #cmd is command
        if cmd == "insert":
            L.insert(int(A[1]),int(A[2]))
        elif cmd == "append":
            L.append(int(A[1]))
        elif cmd == "remove":
            L.remove(int(A[1]))
        elif cmd == "print":
            print(L)
        elif cmd == "pop":
            L.pop()
        elif cmd == "reverse":
            L.reverse()
        elif cmd == "sort": 
            L.sort()
