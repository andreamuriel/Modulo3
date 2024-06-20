import json

def create_stock_file():

    with open("total_stock", "w") as stock_file:
        json.dump({"stock": 0}, stock_file)


create_stock_file()

def get_stock():
    with open("total_stock", "r") as stock_file:
        stock = json.load(stock_file)
        print(f"Stock : {stock["stock"]}")


get_stock()

def create_sales_file():

    with open("total_sales", "w") as sales_file:
        json.dump({"id_employee": 0, "sales": 0, "total_sales": 1000}, sales_file)


create_sales_file()

def get_sales():
    with open("total_sales", "r") as sales_file:
        sales = json.load(sales_file)
        total_comision = sales["total_sales"] * 0.10
        print(f"Comision total por ventas : {total_comision}")


get_sales()

def create_user_file():
    with open("user_info", "w") as user_file:
        json.dump({"username":"", "password":""}, user_file)

create_user_file()

def set_user_info(username, password):
    with open("user_info", "w") as user_file:
        json.dump({"username":username, "password":password}, user_file)
        print(f"User {username} creado correctamente")

set_user_info("Andrea", "123456")


# Identifique claramente la diferencia entre un archivo XML, JSON y YAML.

'''
YAML:
* No tan legilbe como JSON pero mas que XML
* No esta vinculado a ningun lenguaje de programacion especifico
* Ideal para configuraciones y archivos de definiciones

XML:
* Indepependiente respecto al lenguaje de programacion
* formato legible maquina y usuario
* No tan legible como JSON
* No nativo de Python

JSON:
* Similar a un diccionairo de python
* formato legible maquinas y usuarios
* el mas utilizado para APIs

'''