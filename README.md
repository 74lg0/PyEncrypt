# PyEncrypt
### PyEncrypt es un software de encriptacion de texto bastante sencillo, NO ESTA DESTINADO A LA PROTECCION DE DATOS
PyEncrypt utiliza algoritmos de decodificacion de texto bastantes sencillos, ofrece 4 metodos (Creados por mi)
  
## [1] SAN (Sistema Alfa Numerico)
```
Simplemente es el remplazo de letras por su respectiva posicion en el abecedario
asi A = 1, B = 2, C = 3, D = 4, etc
```
![image](https://github.com/74lg0/PyEncrypt/assets/111157836/a01aa9c2-d43a-4ed3-bb8d-3b32a0c9c015)
## [2] SMAN (Sistema de Multiplicación Alfa Numerico)
```
Usa lo mismo que SAN, convierte las letras en numeros respecto al abecedario,
pero con la diferencia de que estos son multiplicados por la cantidad de caracteres, asi:
ABC = 1,2,3
(1,2,3)(Caracteres, en este caso 3) = (3, 6, 9)
```
![image](https://github.com/74lg0/PyEncrypt/assets/111157836/47bcd072-827c-471d-8468-c948862627ba)

## [3] SMPC
```
Similar a SMAN, con la diferencia de que este multiplica los numeros por su respectiva posicion
Asi abc = 1,2,3
(1)(1) = 1
(2)(2) = 4
(3)(3) = 9
abc = 1,4,9
```
![image](https://github.com/74lg0/PyEncrypt/assets/111157836/a1da9d79-d45d-4ab4-8eaf-399412ea093d)

## [4] SMAN + SMPC
```
Simplificado es la union de estos dos metodos
En principio abc = 1,2,3
(1,2,3)(n) = (3, 6, 9)
(3)(1) = 3
(6)(2) = 12
(9)(3) = 27
```
![image](https://github.com/74lg0/PyEncrypt/assets/111157836/2c07e670-af89-42ee-8148-f6208c3001c7)
