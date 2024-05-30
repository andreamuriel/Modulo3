import uuid
import random
import time

#Info de clientes productos y compras de te lo vendo

db_te_lo_vendo = {
    "clientes": {
        str(uuid.uuid1()) + "_piloto": {
            "nombre": "andrea venegas",
            "edad": 25
        },
        str(uuid.uuid1()) + "_piloto": {
            "nombre": "brandon choe",
            "edad": 30
        },
        str(uuid.uuid1()) + "_piloto": {
            "nombre": "nicolas nuñez",
            "edad": 37
        },
        str(uuid.uuid1()) + "_piloto": {
            "nombre": "sandra venegas",
            "edad": 59
        },
        str(uuid.uuid1()) + "_piloto": {
            "nombre": "jose venegas",
            "edad": 51
        },
        str(uuid.uuid1()) + "_piloto": {
            "nombre": "eduardo venegas",
            "edad": 82
        },
        str(uuid.uuid1()) + "_piloto": {
            "nombre": "jose ignacio venegas",
            "edad": 26
        },
        str(uuid.uuid1()) + "_piloto": {
            "nombre": "carolina venegas",
            "edad": 30
        },
        str(uuid.uuid1()) + "_piloto": {
            "nombre": "daniela venegas",
            "edad": 30
        },
        str(uuid.uuid1()) + "_piloto": {
            "nombre": "elisabeth perez",
            "edad": 79
        }
    },
    "productos": {
        str(uuid.uuid1()) + "_piloto": {
            "nombre": "laptop",
            "precio": 299000,
            "color": "verde"
        },
        str(uuid.uuid1()) + "_piloto": {
            "nombre": "xbox",
            "precio": 2499000,
            "color": "negra"
        },
        str(uuid.uuid1()) + "_piloto": {
            "nombre": "ps5",
            "precio": 599000,
            "color": "blanca"
        },
        str(uuid.uuid1()) + "_piloto": {
            "nombre": "nintendo switch",
            "precio": 299000,
            "color": "roja"
        },
        str(uuid.uuid1()) + "_piloto": {
            "nombre": "steam deck",
            "precio": 699000,
            "color": "negra"
        },
    },
    "compras": {
        str(uuid.uuid1()) + "_piloto":{
            "nombre_cliente": "nicolas nuñez",
            "producto": "steam deck",
            "cantidad": 1
        },
        str(uuid.uuid1()) + "_piloto":{
            "nombre_cliente": "andrea venegas",
            "producto": "xbox",
            "cantidad": 1
        },
        str(uuid.uuid1()) + "_piloto":{
            "nombre_cliente": "carolina venegas",
            "producto": "ps5",
            "cantidad": 1
        },
    }
}


#Agregar nuevo cliente 

#nuevo id unico
nuevo_id_cliente = str(uuid.uuid1()) + "_piloto"

#nuevo cliente
nuevo_cliente = {
    "nombre": "ivan coyhaique",
    "edad": 28
}

#Agregar informacion a db_te_lo_vendo
db_te_lo_vendo["clientes"][nuevo_id_cliente] = nuevo_cliente


#Agregar nuevo producto

#nuevo id producto

nuevo_id_producto = str(uuid.uuid1()) + "_piloto"

#nuevo producto

nuevo_producto = {
    "nombre": "legion go",
    "precio": 799000,
    "color": "piano black"
}

#Agregar nuevo producto a db_te_lo_vendo

db_te_lo_vendo["productos"][nuevo_id_producto] = nuevo_producto

#Mostrar clientes

print("\n ** Nombres clientes Te lo Vendo ** \n")
for clientes_id in db_te_lo_vendo["clientes"]:
    cliente = db_te_lo_vendo["clientes"][clientes_id]
    print(f"Nombre cliente: {cliente["nombre"]}")

#Mostrar productos

print("\n ** Listado productos Te lo Vendo ** \n")
for productos_id in db_te_lo_vendo["productos"]:
    producto = db_te_lo_vendo["productos"][productos_id]
    print(f"Nombre Producto : {producto["nombre"]}")

#Elimine clientes. ¿Qué información requiere para eliminar un cliente al azar?
# Se requeire el id del cliente y utilzar un random del indice.

#Eliminar cliente

print("\n ** Eliminando Cliente **")

#Generar un número aleatorio
numero_aleatorio_clientes = random.randint(0, len(db_te_lo_vendo["clientes"]) - 1)

#Eliminar el elemento aleatorio
cliente_eliminado = db_te_lo_vendo["clientes"].pop(list(db_te_lo_vendo["clientes"].keys())[numero_aleatorio_clientes])

print(f"** Cliente eliminado {cliente_eliminado} **")

#Productos. ¿Qué información requiere para eliminar el último producto agregado?
#Con el metodo popItem() puedo acceder al ultimo elemento y eliminarlos de productos 

#Eliminar producto

print("** Eliminando Producto **")

# Eliminar el elemento aleatorio
producto_eliminado = db_te_lo_vendo["productos"].popitem()

print(f"** Producto eliminado {producto_eliminado} **")


print("** Listado de clientes y productos actualizado ** \n")

#Valores clientes, con delay 3 seg

print("** Valores de clientes ** \n")
for clientes_id in db_te_lo_vendo["clientes"]:
    time.sleep(3)
    cliente = db_te_lo_vendo["clientes"][clientes_id]
    print(f"Nombre cliente valor: {cliente["nombre"]}")
    print(f"Edad cliente valor : {cliente["edad"]}")

#Valores productos,con delay 3 seg

print("\n ** Valores de productos ** \n")
for productos_id in db_te_lo_vendo["productos"]:
    time.sleep(3)
    producto = db_te_lo_vendo["productos"][productos_id]
    print(f"Nombre producto valor : {producto["nombre"]}")
    print(f"Precio producto valor : {producto["precio"]}")
    print(f"Color producto valor : {producto["color"]}")
    
#claves productos, con delay 2 seg

print("** Claves de clientes ** \n")
for clientes_id in db_te_lo_vendo["clientes"]:
    time.sleep(2)
    cliente = db_te_lo_vendo["clientes"][clientes_id]
    for clave in cliente.keys():
        print(f"Claves Clientes {clave}")



print("\n ** claves de productos ** \n")
for productos_id in db_te_lo_vendo["productos"]:
    time.sleep(2)
    producto = db_te_lo_vendo["productos"][productos_id]
    for clave in producto.keys():
        print(f"Claves Productos {clave}")
    

print("** Mostrando ID de usuarios **")
for id_usuario in db_te_lo_vendo["clientes"]:
    print(f"ID: {id_usuario}")
    


#Eliminar los ultimos 4 clientes
claves_clientes = list(db_te_lo_vendo["clientes"].keys())
ultimos_cuatro = claves_clientes[-4:]

for clave in ultimos_cuatro:
    id_eliminado = clave
    del db_te_lo_vendo["clientes"][clave]
    print(f"ID Elimnado {id_eliminado}")