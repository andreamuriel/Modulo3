class Compra:
    def __init__(self, id_compra, cliente, productos, total):
        self.id_compra = id_compra
        self.cliente = cliente
        self.productos = productos
        self.total = None

    def agregar_producto(self, producto, cantidad):
        print("Agregar producto a carrito")
        if producto.stock >= cantidad:
            producto.stock -= cantidad
            self.productos.append((producto, cantidad))
            return True
        else:
            print(f"No hay suficiente stock de {producto.nombre}")
            return False

    def eliminar_producto(self, producto, cantidad):
        print("Eliminar producto")
        for prod in self, producto:
            if prod == producto:
                prod.stock += cantidad
                self.productos.remove((prod))
            else:
                print("No hay suficiente stock del producto")
                return False

    def calcular_total(self):
        print("Calcular total compra")
        total = sum(prod.valor_neto * cantidad for prod, cantidad in self.productos)
        return total

    def detalle_compra(self):
        return f"Compra: {self.id_compra}, Cliente: {self.cliente.nombre}, Total: {self.total}"
