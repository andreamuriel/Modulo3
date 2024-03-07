#Para definir los precios de cada producto se creó un diccionario que contiene el nombre de cada producto y su respectivo precio.
productos = {
    "Producto1": 1000.0,
    "Producto2": 2000.0,
    "Producto3": 3000.0,
    "Producto4": 4000.0,
    "Producto5": 5000.0,
}

#Para la solicitud de la cantidad de cada producto se creó un diccionario para contener la cantidad de productos seleccionados por el usuario.
cantidad_pedidos = {}

for producto, valor_unitario in productos.items():
    print("Bienvenido a Te Lo Vendo")
    cantidad = int(input(f"Ingrese la cantidad de {producto}: "))
    cantidad_pedidos[producto] = cantidad

total_neto = sum(cantidad_pedidos[producto] * valor_unitario for producto, valor_unitario in productos.items())

iva = total_neto * 0.19

total_final = total_neto + iva

print(f"\nResumen del pedido:")
for producto, cantidad in cantidad_pedidos.items():
    print(f"{producto}: {cantidad} unidades")

print(f"\nTotal neto: ${total_neto} CLP")
print(f"Total IVA (19%): ${iva} CLP")
print(f"Total final del pedido: ${total_final} CLP")