"""
Find a String
imprimir el numero de veces que el substring esta dentro
del string


ABCDCDC     len()=7
CDC         len()=3

Se puede hacer con startwith() pero lo quiero hacer nativo
para entender mejor la sintaxis y tiene un orden logico con el 
desafio anterior. 

si una sintaxis de corte (o slicing)
[:x] extrae los primeros x elementos de una secuencia, se detiene 
justo en la posicion x, no incluye el indice numero x. 
y esta el [x:y]
corta la lsita desde x hasta y-1
---
si tomo la cantidad del pedazo del string por cada paso como seria ? 
string[:len(sub_string)]
---
debo hacer un puntero para contar, sera count
---
este pedazo se debe leer en todo el string len(string)
pero esta limitado y no completara todo por lo tanto tendra menos len(sub_string)
---
lo explico mejor asi: 
Ejemplo: s = "ABCDCDC", sub = "CDC"

i=0: |ABC|DCD  →  ABC ≠ CDC
i=1:  A|BCD|CD →  BCD ≠ CDC
i=2:  AB|CDC|D →  CDC = CDC  ✓ count += 1
i=3:  ABC|DCD|  →  DCD ≠ CDC

en el i=5 no peudo seguir mas, para que es perdida de computo por lo tanto
range deberia quedar asi: range(len(string)-len(sub_string)+1)
se suma un valor porque siempre cuenta menos uno 
---
ahora como se debe identificar el fragmento desde i hacia adelante? 
y si el desafio te da diferentes tamanhos de sub_string: 
⇒ A[i:len(sub_string)] esto nos quiere decir que en el indice i seleccionado en el bucle, hasta la extension del len(sub_string).
debo agregar desde el indice i + la cantidad de len()
esto dentro de una condicional if

"""

# asi queda el codigo
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            count+=1
    return count        

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)