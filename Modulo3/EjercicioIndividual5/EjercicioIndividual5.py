# Creacion Id unicos
import uuid


#¿Qué problemas encontró con esta forma de almacenar la información?

#Se encontraron problemas respecto al manejo de la información y al acceso a ellos, 
#se vuelve mucho más compleja su manipulación y acceso a los datos específicos.


#Diccionarios

andrea = {
    "nombre": "andrea venegas",
    "edad": 25,
    "genero": "femenino",
    "direccion": "calle falsa 123",
    "telefono": "912345678",
    "nacionalidad": "chilena"
}

nicolas = {
    "nombre": "nicolas nuñez",
    "edad": 37,
    "genero": "masculino",
    "direccion": "calle falsa 134",
    "telefono": "912345679",
    "nacionalidad": "chilena"
}

brandon = {
    "nombre": "brandon choe",
    "edad": 30,
    "genero": "masculino",
    "direccion": "calle falsa 135",
    "telefono": "912345670",
    "nacionalidad": "chilena"
}

elisabeth = {
    "nombre": "elisabeth perez",
    "edad": 79,
    "genero": "femenino",
    "direccion": "calle falsa 126",
    "telefono": "912345671",
    "nacionalidad": "chilena"
}

tahis = {
    "nombre": "tahis godoy",
    "edad": 25,
    "genero": "femenino",
    "direccion": "calle falsa 127",
    "telefono": "912345672",
    "nacionalidad": "chilena"
}

eduardo = {
    "nombre": "eduardo arriagada",
    "edad": 82,
    "genero": "masculino",
    "direccion": "calle falsa 156",
    "telefono": "912345673",
    "nacionalidad": "chilena"
}

eric = {
    "nombre": "eric venegas",
    "edad": 3,
    "genero": "masculino",
    "direccion": "calle falsa 167",
    "telefono": "912345674",
    "nacionalidad": "chilena"
}

#Almacenar diccionarios en una lista

JJVV= [andrea, nicolas, brandon, elisabeth, tahis, eduardo, eric]

#Recorrer lista

for vecino in JJVV:
    print("** Usuario Junta de vecinos ** \n")
    print(f"Nombre: {vecino["nombre"]} \n")
    print(f"Edad: {vecino["edad"]} \n")
    print(f"Genero: {vecino["genero"]} \n")
    print(f"Direccion: {vecino["direccion"]} \n")
    print(f"Telefono: {vecino["telefono"]} \n")
    print(f"Nacionalidad: {vecino["nacionalidad"]} \n")
    
    

# Estructura de Datos Unificada

JJVV_unified = [{
    "nombre_junta": "Junta vecinos Frankfort",
    "id_unico": uuid.uuid1(),
    "usuarios": [
        {
            "id":uuid.uuid1(),
            "nombre": "andrea venegas",
            "edad": 24,
            "genero": "masculino",
            "direccion": "av 9 norte 336",
            "telefono": "344556755",
            "nacionalidad": "chilena",
            "antigüedad": 2,
            "fecha_incorporacion": "2024-01-01"
        },
        {
            "id": uuid.uuid1(),
            "nombre": "nicolas nuñez",
            "edad": 29,
            "genero": "femenino",
            "direccion": "av 7 norte 337",
            "telefono": "222233777444",
            "nacionalidad": "chilena",
            "antigüedad": 2,
            "fecha_incorporacion": "2024-01-01"
        }
    ]
},
{
    "nombre_junta": "Junta vecinos Grecia",
    "id_unico": uuid.uuid1(),
    "usuarios": [
        {
            "id": uuid.uuid1(),
            "nombre": "brandon choe",
            "edad": 22,
            "genero": "masculino",
            "direccion": "av 2 norte 339",
            "telefono": "334554567777",
            "nacionalidad": "chilena",
            "antigüedad": 2,
            "fecha_incorporacion": "2024-01-01"
        },
        {
            "id": uuid.uuid1(),
            "nombre": "elisabeth perez",
            "edad": 33,
            "genero": "masculino",
            "direccion": "av nueve norte 653",
            "telefono": "678888885",
            "nacionalidad": "chilena",
            "antigüedad": 2,
            "fecha_incorporacion": "2024-01-01"
        },
        {
            "id": uuid.uuid1(),
            "nombre": "tahis godoy",
            "edad": 44,
            "genero": "femenino",
            "direccion": "av 3 norte 889",
            "telefono": "999976654",
            "nacionalidad": "chilena",
            "antigüedad": 2,
            "fecha_incorporacion": "2024-01-01"
        },
        {
            "id": uuid.uuid1(),
            "nombre": "eduardo arriagada",
            "edad": 55,
            "genero": "femenino",
            "direccion": "av 4 norte 144",
            "telefono": "45665777",
            "nacionalidad": "chilena",
            "antigüedad": 2,
            "fecha_incorporacion": "2024-01-01"
        },
        {
            "id": uuid.uuid1(),
            "nombre": "eric venegas",
            "edad": 34,
            "genero": "femenino",
            "direccion": "av 5 norte 673",
            "telefono": "2222444566",
            "nacionalidad": "chilena",
            "antigüedad": 2,
            "fecha_incorporacion": "2024-01-01"
        }            
    ]                 
}                
]


#Mostrar fecha de incorporacion de los usuarios a junta de vecinos
for junta_vecinos in JJVV_unified:
    print(f" ** Junta de Vecinos : {junta_vecinos["nombre_junta"]}")
    for usuario_junta in junta_vecinos["usuarios"]:
        print(f"Fecha de incorporacion {usuario_junta["nombre"]}: {usuario_junta["fecha_incorporacion"]}")
      