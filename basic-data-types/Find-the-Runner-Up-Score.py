# Find the Runner-Up Score!

"""

Se da el numeo de participantes para el dia de deportes universitario. 
Debo encontrar el segundo luga. En ingles es Runner-up score

usar funcion sorted() 
y obtener el segundo indice de la lista con arr[1]
todo esto dentrode la funcion print()

--------------

por ejemplo se podrian repetir valores que son mayores que el segundo lugar, por lo tanto se usa set()
con el orden sorted() es ascendente, no descendente entonces no me sirve. Debo darlo vuelta con [::-1]
asi queda: 
    runner_up = sorted(set(arr))[::-1]
ahora donde agregue que se obtenga el segundo lugar es con [1], en la variable runner_up

"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    runner_up = sorted(set(arr))[::-1]
    print(runner_up[1])