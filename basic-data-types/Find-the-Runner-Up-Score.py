# Find the Runner-Up Score!

"""
Se da el numeo de participantes para el dia de deportes universitario. 
Debo encontrar el segundo luga. En ingles es Runner-up score

usar funcion sorted() 
y obtener el segundo indice de la lista con arr[1]
todo esto dentrode la funcion print()
"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    runner_up = sorted(arr)
    print(runner_up[1])