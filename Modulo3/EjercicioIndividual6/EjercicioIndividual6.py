import getpass
import time

users = []


def create_user():
    edad = ""
    print("## Creacion de usuario ##")
    username = input("Ingrese el nombre de usuario: ")
    password = getpass.getpass("Ingrese password: ")
    while not edad.isdigit():
        edad = input("Ingrese su edad (Solo numeros): ")
    edad = int(edad)
    
    users.append({"username": username, "password": password, "edad": edad})
    
def user_info():
    print("## Informacion de usuarios ## \n")
    for user in users:
        print(f"Nombre usuario: {user["username"]}")
        print(f"Contraseña: {user["password"]}")
        print(f"Edad:  {user["edad"]} \n")
        time.sleep(5)
    
while True:
    create_user()
    salir = input("Si desea salir del programa ingrese (salir) o presione enter para continuar: ")
    if salir:
        user_info()
        break
