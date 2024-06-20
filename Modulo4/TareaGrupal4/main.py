class Sucursal:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.stock = 30

    def validar_stock(self):
        if self.stock < 50:
            print("Se esta solicitando y reponiendo productos")
            return True
        else:
            print("No es necesario reponer stock suficiente")
            return False


class Bodega(Sucursal):
    def __init__(self, nombre, direccion, stock_total):
        super().__init__(nombre, direccion)
        self.stock_total = stock_total

    def reponer_stock(self):
        if self.stock_total < 300:
            print("El stock actual de la bodega es insufiente para satisfacer la reposición")
        else:
            self.stock_total -= 300
            self.stock += 300
            print("Se descontaron 300 productos del stock de la bodega y se asignaron a la sucursal")
            print(f"Stock actual en la bodega: {self.stock_total}")
            print(f"Stock actual en la sucursal: {self.stock}")


# Crear una bodega
bodega1 = Bodega(nombre="Bodega Central", direccion="Calle falsa 123", stock_total=500)

# Crear una sucursal
sucursal1 = Sucursal(nombre="Sucursal Sur", direccion="Avenida siempre viva 1234")
sucursal2 = Sucursal(nombre="Sucursal Norte", direccion="Holanda 8756")

# Llamando metodos
if sucursal1.validar_stock():
    bodega1.reponer_stock()

if sucursal2.validar_stock():
    bodega1.reponer_stock()


class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


class OrdenCompra:
    def __init__(self, id_ordencompra, producto, despacho):
        self.id_ordencompra = id_ordencompra
        self.producto = producto
        self.despacho = despacho

    def valor_final(self):
        valor_neto = self.producto.precio
        impuesto = valor_neto * 0.19
        total = valor_neto + impuesto

        if self.despacho:
            total += 5000

        print(f"El valor total de la compra es: {total}")
        return total


# Crear producto
producto1 = Producto(nombre="Xbox Series X", precio=399000)
producto2 = Producto(nombre="PS5", precio=499000)

# Crear una orden de compra
orden1 = OrdenCompra(id_ordencompra=1, producto=producto1, despacho=True)
orden1.valor_final()

orden2 = OrdenCompra(id_ordencompra=2, producto=producto2, despacho=False)
orden2.valor_final()
