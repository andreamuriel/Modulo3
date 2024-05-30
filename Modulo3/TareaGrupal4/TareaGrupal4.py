import random
import time

productos = {"PS5": 120, "XBOX": 150}
contador_ventas = 0
max_stock = 0

def buy_product(compra_producto, items_a_comprar):
    global contador_ventas
    if compra_producto in productos:
        if productos[compra_producto] >= items_a_comprar:
            productos[compra_producto] -= items_a_comprar
            contador_ventas += 1
            cuenta_venta_productos()
        else:
            print(f"No hay suficiente stock de {compra_producto}")
    else:
        print("El producto no existe en el inventario.")

def cuenta_venta_productos():
    global contador_ventas
    if contador_ventas == 10:
        print("Se han realizado 10 ventas, por lo que se informará del stock de los productos")
        print(f"XBOX - Stock: {productos['XBOX']} PS5 - Stock: {productos['PS5']}")
        contador_ventas = 0

def verificar_stock():
    global max_stock
    if max_stock < 150:
        if productos["PS5"] < 100:
            productos["PS5"] += 50
            max_stock += 50
            print("Se adicionaron 50 productos más de stock a PS5")
        if productos["XBOX"] < 100:
            productos["XBOX"] += 50
            max_stock += 50
            print("Se adicionaron 50 productos más de stock a XBOX")
    else:
        print("Se alcanzó el límite de abastecimiento")

def compra_random():
    product_choice = ["XBOX", "PS5"]
    random_product = random.choice(product_choice)
    items_a_comprar = random.randint(1, 10)
    print(f"Items a comprar: {items_a_comprar} del producto {random_product}")
    time.sleep(3)
    verificar_stock()
    buy_product(random_product, items_a_comprar)

while productos["PS5"] > 0 or productos["XBOX"] > 0:
    compra_random()

print("No hay más productos en stock")