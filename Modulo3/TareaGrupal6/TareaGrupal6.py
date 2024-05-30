import uuid

#Productos
products = [
    {
        "id": 1,
        "name": "laptop",
        "stock": 30,
    },
    {
        "id": 2,
        "name": "ps5",
        "stock": 30,
    },
    {
        "id": 3,
        "name": "xbox",
        "stock": 50,
    },
    {
        "id": 4,
        "name": "nintendo switch",
        "stock": 30,
    },
    {
        "id": 5,
        "name": "steam deck",
        "stock": 45,
    },
    {
        "id": 6,
        "name": "rog ally",
        "stock": 30,
    },
    {
        "id": 7,
        "name": "lenovo go",
        "stock": 30,
    },
]

# #####[INICIO CONTROL DE BODEGA]#####

#Función agregar productos
def add_new_products():
    print("## Agregar nuevo producto ##")
    product_name = input("* Ingrese nombre producto: ")
    product_stock = ""
    while not product_stock.isdigit():
        product_stock = input(
            "** Ingrese cantidad de stock de productos (Solo numeros) : "
        )

    products.append(
        {"id": str(uuid.uuid1()), "name": product_name, "stock": product_stock}
    )
    print("** Producto agregado **")

#Función actualizar stock  producto
def stock_update():
    print("## Actualizacion stock de productos ##")
    product_update = input("** Ingresa el nombre del producto: ")
    if any(product["name"] == product_update for product in products):
        stock_update = ""
        while not stock_update.isdigit():
            stock_update = input(
                "** Ingrese cantidad de stock de productos a actualizar (Solo numeros): "
            )
        for product in products:
            if product["name"] == product_update:
                product["stock"] = stock_update
                print("** Stock actualizado **")
    else:
        print("** Prodcuto ingresado no existe **")

#Función que muestra stock de todos los productos 
def stock_availability():
    print("## Disponibilidad de productos ## ")
    print("## Stock de productos ##")
    print("-" * 30)
    for product in products:
        print(f"Nombre : {product["name"]}")
        print(f"Stock : {product["stock"]} \n")

    products_list = []
    for product in products:
        products_list.append({"nombre": product["name"], "stock": product["stock"]})
    return products_list

#Función que muestra el stock de un producto en particular
def stock_availability_name():
    print("## Consulta stock de producto por nombre ##")
    product_name = input("** Ingresa nombre de producto : ")
    if any(product["name"] == product_name for product in products):
        print("## Disponibilidad de producto ## ")
        print("## Stock de producto ##")
        print("-" * 30)
        for product in products:
            if product["name"] == product_name:
                print(f"Nombre : {product["name"]}")
                print(f"Stock : {product["stock"]} \n")
    
    product_found = False
    for product in products:
        if product["name"] == product_name:
            product_found = True
            return {"nombre": product["name"], "stock": product["stock"]}

    if not product_found:
        print(f"** Producto {product_name} no encontrado. **")
        return None
                
#Función que muestra los productos
def product_all():
    print("## Listado de productos de la tienda ##")
    print("## Productos ##")
    print("-" * 30)
    
    for product in products:
        print(f"**- {product["name"]} ")
    
    products_list = []
    for product in products:
        products_list.append(product["name"])
    return products_list

#Función que muestra productos con un stock superior al ingresado
def product_by_stock():
    stock_product = ""
    while not stock_product.isdigit():
        stock_product = input("** Ingrese cantidad de stock(Solo numeros): ")
    
    print("## Listado de productos de la tienda ##")
    print("Se mostrarán productos con stock superior al ingresado")
    print("## Productos ##")
    print("-" * 30)
    for product in products:
        if product["stock"] > int(stock_product):
            print(f"**- {product["name"]} ")
    
    products_list = []
    for product in products:
        if product["stock"] > int(stock_product):
            products_list.append(product["name"])
    return products_list     

# #####[TERMINO CONTROL DE BODEGA]#####

#######################################

clients = [
    {
        "id": 1,
        "nombre": "jorge perez",
    },
    {
        "id": 2,
        "nombre": "claudio jerez",
    },
    {
        "id": 3,
        "nombre": "pablo marmol",
    },
    {
        "id": 4,
        "nombre": "pedro picapiedra",
    },
    {
        "id": 5,
        "nombre": "betty marmol",
    }
]

sells = []

# #####[INICIO CONTROL DE VENTAS]#####

def register_clients():
    print("## Clientes Registrados ## \n")
    quantity_clients = len(clients)
    print(f"La cantidad de clientes registrados en la tienda son : {quantity_clients}")
    return f"La cantidad de clientes registrados en la tienda son : {quantity_clients}"
    
def product_request():
    print("## Solicitar una compra ##")
    id_client = input("Ingrese ID Cliente : ")
    id_product = input("Ingrese ID de Producto :  ")
    quantity_product = 1
    
    sells.append({"id_cliente": id_client, "id_producto": id_product, "cantidad": quantity_product})
    print("\n ** Solicitud de compra realizada **")
    return "\n ** Solicitud de compra realizada **"
    
def stock_verify(id_product, quantity):
  for product in products:
    if product["id"] == id_product:
      return product["stock"] >= quantity
  return False

    
def authorize_purchase(id_product, quantity):
  if stock_verify(id_product, quantity):
    return "Compra aprobada y en camino"
  else:
    return "Compra cancelada"

# #####[TERMINO CONTROL DE VENTAS]#####

#Menú principal
def main():
    while True:
        print("\n## Menú de la tienda ##")
        print("1. Agregar nuevo producto")
        print("2. Actualizar stock de producto")
        print("3. Mostrar stock de todos los productos")
        print("4. Mostrar stock de un producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Mostrar productos con stock superior a una cantidad")
        print("7. Registrar clientes")
        print("8. Solicitar una compra")
        print("9. Salir")
        
        choice = input("Seleccione una opción: ")
        
        if choice == '1':
            add_new_products()
        elif choice == '2':
            stock_update()
        elif choice == '3':
            stock_availability()
        elif choice == '4':
            stock_availability_name()
        elif choice == '5':
            product_all()
        elif choice == '6':
            product_by_stock()
        elif choice == '7':
            register_clients()
        elif choice == '8':
            product_request()
        elif choice == '9':
            print("Saliendo del programa... nos vemos")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()