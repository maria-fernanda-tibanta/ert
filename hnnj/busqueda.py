## EPN-ESFOT-ASI Algoritmos Fundamentales 2016-B

## busca_en_lista.py
## Versión: 1.0
## Búsqueda de un elemento en una lista

## Autor: María Fernanda Tibanta
## Fecha: 04-Nov-2016

## Creación de lista
lista = []
elemento = input("ingrese un nuevo elemento de la lista: ")
while elemento != "":
    lista.append(elemento)
    elemento = input("ingrese un nuevo elemento de la lista: ")
print("La lista generada es: ", lista)

## Pide la palabra a buscar
palabra = input("Ingrese la palabra que desea buscar: ")

## BUSCA LA PALABRA

##Método 1: Usa funciones incorporadas en Python
print("\n## Método 1: Usa funciones incorporadas en Python")
print (palabra in lista)    # función booleana

if palabra in lista:
    print ("la palabra", palabra, "fue encontrada en la lista", lista)
else:
    print ("la palabra", palabra, "NO fue encontrada en la lista", lista)

## Método 2: Recorre la lista al estilo Python
print("\n## Método 2: Recorre la lista al estilo Python")
for elemento in lista:
    if elemento == palabra:
        print ("la palabra", palabra, "corresponde al elemento", elemento)
    else:
        print ("la palabra", palabra, "NO corresponde al elemento", elemento)

## Método 3: Recorre la lista al estilo Java o C++
print("\n## Método 3: Recorre la lista al estilo Java o C++")
n = len(lista)
for i in range(n):
    if lista[i] == palabra:
        print ("la palabra", palabra, "corresponde al elemento", i, "que es", lista[i])
    else:
        print ("la palabra", palabra, "NO corresponde al elemento", i, "que es", lista[i])
