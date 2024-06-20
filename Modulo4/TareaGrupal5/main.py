from excepciones import StockInsuficienteError


class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


class Sucursal:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.stock = 30

    def validar_stock(self):
        if self.stock < 50:
            print("Se está solicitando y reponiendo productos")
            return True
        else:
            print("No es necesario reponer, stock suficiente")
            return False


class Bodega(Sucursal):
    def __init__(self, nombre, direccion, stock_total):
        super().__init__(nombre, direccion)
        self.stock_total = stock_total

    def reponer_stock(self):
        try:
            if self.stock_total < 300:
                raise StockInsuficienteError("El stock insuficiente para satisfacer la reposición")
            else:
                self.stock_total -= 300
                self.stock += 300
                print("Se descontaron 300 productos del stock de la bodega y se asignaron a la sucursal")
                print(f"Stock actual en la bodega: {self.stock_total}")
                print(f"Stock actual en la sucursal: {self.stock}")
        except StockInsuficienteError as e:
            print(e)
        finally:
            print("-" * 80)


class CarroCompras:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto, cantidad):
        if cantidad > 10:
            raise ValueError("No puedes comprar más de 10 unidades de un producto.")
        if producto in self.productos:
            self.productos[producto] += cantidad
        else:
            self.productos[producto] = cantidad

    def mostrar_carro(self):
        print("Contenido del carro de compras:")
        for producto, cantidad in self.productos.items():
            print(f"{producto}: {cantidad} unidades")

    def valor_promedio_compras(self, cliente):
        try:
            total_compras = sum(cliente.compras)
            promedio = total_compras / len(cliente.compras)
            return promedio
        except ZeroDivisionError:
            print("El cliente no tiene compras aún.")
            return 0


class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.compras = []

    def agregar_compra(self, monto):
        self.compras.append(monto)


if __name__ == "__main__":

    bodega1 = Bodega(nombre="Bodega Central", direccion="Calle falsa 123", stock_total=1000)
    sucursal1 = Sucursal(nombre="Sucursal Sur", direccion="Avenida siempre viva 1234")
    sucursal2 = Sucursal(nombre="Sucursal Norte", direccion="Holanda 8756")

    if sucursal1.validar_stock():
        bodega1.reponer_stock()

    if sucursal2.validar_stock():
        bodega1.reponer_stock()

    cliente1 = Cliente("Camilo")
    cliente1.agregar_compra(55000)
    cliente1.agregar_compra(22000)

    carro = CarroCompras()
    try:
        carro.agregar_producto("Camiseta", 5)
        carro.agregar_producto("Pantalón", 12)
        carro.agregar_producto("Zapatos", 3)
    except ValueError as e:
        print(e)

    carro.mostrar_carro()
