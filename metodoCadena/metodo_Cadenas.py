cadena1 = "hola Mundo"
cadena2 =  "Bienvenido maquinola"
#   Estructura del metodo:
# dato.metodo()
# convierte la cadena de texto a mayuscula
resultado = cadena1.upper()

# convierte la cadena de texto a minuscula
resultado2 = cadena2.lower() 

# convierte la 1ra letra de la cadena en mayuscula y las demas a minuscula
resultado3 = cadena1.capitalize() 

# devuelve la posición donde se encontro el caracter
busquedaLetra = cadena1.find("Mu") # Si no encuentra resultados devuelve un -1

# devuelve la posición donde se encontro el caracter
busqueda_Index = cadena1.index("Mu") # Si no encuentra coincidencias da un error, necesita excepciones

print(resultado)
print(resultado2)
print(resultado3)
print(busquedaLetra)

