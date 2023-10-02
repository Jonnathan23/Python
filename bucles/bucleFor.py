

datosCliente = {
    "nombre" :"Fernando",
    "edad" : 12
}
seresVivos = ['perro','vaca','cocodrilo']

#Recorre una lista
for animal in seresVivos:
    print(animal)
else:
    print(" - El bucle termino")
    
conjunto = ['perro', 45]
print(" ---------")
#Para Arreglos asociados
for key in datosCliente.items():
    print(key)
print(" ---------")
#Si no se ejecuta de la forma anterior solo nos va a entregar el nombre con el que se asoció el dato
for key in datosCliente:
    print(key)
