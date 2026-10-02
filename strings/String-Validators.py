
"""
-- String Validators --

str.isalnum() // Este método comprueba si todos los caracteres de una cadena son alfanuméricos (az, AZ y 0-9) .
str.isalpha() // Este método comprueba si todos los caracteres de una cadena son alfabéticos (az y AZ) .
str.isdigit() // Este método comprueba si todos los caracteres de una cadena son dígitos (0-9) .
str.islower() // Este método comprueba si todos los caracteres de una cadena son caracteres en minúscula (az) .
str.isupper() // Este método comprueba si todos los caracteres de una cadena son caracteres en mayúscula (AZ) .

se da una cadena S
En la primera línea, imprime True si tiene algún carácter alfanumérico . De lo contrario, imprime False.
En la segunda línea, imprime True si tiene algún carácter alfabético . De lo contrario, imprime False.
En la tercera línea, imprime True si tiene algún dígito . De lo contrario, imprime False.
En la cuarta línea, imprime True si tiene algún carácter en minúscula . De lo contrario, imprime False.
En la quinta línea, imprime True si tiene caracteres en mayúscula . De lo contrario, imprime False.

"""

if __name__ == '__main__':
    s = input()
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))

    
