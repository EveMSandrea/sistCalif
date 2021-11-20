"""
Sistema de Calificacion Colombiano Vs Sistema de Calificacion Americano
nombre:Evelin Melendez as Eve
correo:sandreaeve.rb@gmail.com
Grupo:98
12 Junio 2021,
"""
import funcionCalificaciones as funCa
print("Bienvenidos a la Institucion Educativa Mision Tic 2022")
print("Sistema de Gestión Académica y Administrativa")
print("===============================================")
"""
Error que se genera en prueba unitaria (EOFError)error de fin de lectura de archivo pero solo ocurre en pruebas unitarias.
"""
nota_final=""
# try quiere decir -intenta- gestionar esto sino salta
try:
 nota_final=str(input("Por favor ingrese la Nota Final: "))
except (EOFError):
#Sino lo puede gestionar comienza a leer aqui  
  nota_final=0.0
# Esta condicional valida que el dato no sea string
if funCa.isFloat(nota_final):
   print("Disculpe introduzca un valor valido de 0.0 a 5.0 ...")
 # Esta condicional valida el rango de notas exigido
elif funCa.isValueRangoNota(float(nota_final)):      
  mensaje_calificacion_colombiano= funCa.determinar_notificacion(float(nota_final))
  mensaje_calificacion_americano=funCa.conversion_sistema_americano(float(nota_final))
print("Para la calificacion Colombiana: ", mensaje_calificacion_colombiano)
print("La conversion de tu calificacion al sistema Americano corresponde la letra: ", mensaje_calificacion_americano)
