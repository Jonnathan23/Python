import modSaludar as saludar
from otrasFunciones.sumatoria import sumatoria as sumar# Forma más espeficia para evitar importaciones que no se vayan a utilizar, ademas importa un modulo que se encuentre dentro de otra carpeta
import sys
sys.path.append("C:\\Users\\jsaqu\\OneDrive\\Escritorio\\Archivos Respaldo\\Jonna Archivos\\Progrmacion python")
import FuncionAfuera
#print(sys.path)
print(saludar.saludar("Fernando"))
print(f'El resultado es: {sumar(3,6,2,2)}')
print(FuncionAfuera.saludarAfuera("Jaime"))