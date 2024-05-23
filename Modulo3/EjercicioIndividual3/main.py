def determinar_cuestionarios(origen, edad, deportes):

  cuestionarios = []
 
  if origen.lower() in ["america latina"]:
    cuestionarios.append("Hábitos alimenticios")

  if 18 <= edad <= 29:
    cuestionarios.append("Empleabilidad")

  if origen.lower() in ["america latina"] and 30 <= edad <= 59:
    cuestionarios.append("Experiencia laboral")

  if origen.lower() in ["america latina"] and edad >= 60:
    cuestionarios.append("Actividades recreativas")

  if deportes and edad < 60:
    cuestionarios.append("Atletismo")

  if deportes and origen.lower() in ["america latina"] and edad >= 60:
    cuestionarios.append("Natación")

  if not deportes:
    cuestionarios.append("Deportes en General")

  if len(cuestionarios) > 3:
    print("¡Has superado el límite de cuestionarios! Solo puedes responder 3.")
    return cuestionarios

  return cuestionarios

origen = input("Ingrese su region de origen: (america latina o no) ")
edad = int(input("Ingrese su edad: "))
deportes = input("¿Tiene afinidad por los deportes? (si/no): ")

cuestionarios = determinar_cuestionarios(origen, edad, deportes)

print(f"Usted debe responder {len(cuestionarios)} cuestionarios:")
for cuestionario in cuestionarios:
  print(f"- {cuestionario}")
