# -*- coding: utf-8 -*-
"""Lab2-Andrés-Cabezas-Vizcaíno.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17GTInCPawAtN4g1lgwbQzXKDV7TQbDPX
"""

print("------------------------------")
print("EJEMPLO2: IMPRIMIR EL MENOR DE DOS NUMEROS")
print("------------------------------")
print("Ingrese 2 Números: ")
x = int( input("Primer Numero: "))
y = int( input("Segundo Numero: "))
print("\nSALIDA:")
print("------------------------------")
if x > y:
  print("El menor es: ",y)
else:
  print("El menor es :",x)

switcher={1:"Enero",2:"Febrero",3:"Marzo",4:"Abril",5:"Mayo",6:"Junio",7:"Julio",8:"Agosto",9:"Septiembre",10:"Octubre",11:"Noviembre",12:"Diciembre"}
argument=int(input("Ingrese un número:"))
nameMes=switcher.get(argument,"Mes inválido")
print(nameMes)