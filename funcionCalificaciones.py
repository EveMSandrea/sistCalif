#funcion para evaluar calificacion Colombiana
def determinar_notificacion(nota_final):
  mensaje=""
  if nota_final > 3.0:
   mensaje="gana"
  if nota_final < 3.0 and nota_final>= 2.2:
   mensaje="recupera" 
  if nota_final <2.2:
    mensaje="pierde"
  return mensaje
"""
funcion para realizar la conversion de la calificacion Colombiana
al Sistema de Evaluacion Americano,Se nombran dos variable de nombre
(conversion y baseCalificada) para realizar la conversion
""" 
def conversion_sistema_americano(nota_final):
  letra_nota=""
  baseCalificada=5
  conversion=(nota_final*100)/baseCalificada
  print(conversion)
  if conversion>=90.0:
    letra_nota="A"
  if conversion>=80 and conversion<90:
    letra_nota="B"
  if conversion>=70 and conversion<80:
    letra_nota="C"
  if conversion>=69 and conversion<70:
    letra_nota="D"
  if conversion<69:
    letra_nota="F"
  return letra_nota
#dos funcion para evaluar lo que introduce el usuario
def isFloat(input_nota):
  try: 
    float(input_nota)
    return False
  except ValueError:
    return True
def isValueRangoNota(nota):
  if float(nota) <0.0:
      return False
  elif float(nota)>=5.1:
      return False
  else:
    return True