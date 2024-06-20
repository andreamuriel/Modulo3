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
                raise IndexError("El stock actual de la bodega es insuficiente para satisfacer la reposición")
            else:
                self.stock_total -= 300
                self.stock += 300
                print("Se descontaron 300 productos del stock de la bodega y se asignaron a la sucursal")
                print(f"Stock actual en la bodega: {self.stock_total}")
                print(f"Stock actual en la sucursal: {self.stock}")
        except IndexError as e:
            print(e)
        except TypeError as e:
            print(e)
        except KeyError as e:
            print(e)
        finally:
            print("-" * 80)


# Crear una bodega
bodega1 = Bodega(nombre="Bodega Central", direccion="Camino Melipilla 655", stock_total=500)

# Crear una sucursal
sucursal1 = Sucursal(nombre="Sucursal Plaza Oeste", direccion="Américo Vespucio 789")
sucursal2 = Sucursal(nombre="Sucursal Plaza Vespucio", direccion="Américo Vespucio 1123")

# Llamando métodos
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
        try:
            valor_neto = self.producto.precio
            impuesto = valor_neto * 0.19
            total = valor_neto + impuesto
            print(f"Valor total de la orden de compra: ${total:.2f}")
            return total
        except TypeError:
            print("El precio no es valido")
        except Exception as e:
            print(f"Error inesperado: {e}")

        finally:
            print("-" * 80)


# Crear un producto
producto1 = Producto(nombre="PS5", precio=499000)

# Crear una orden de compra
orden1 = OrdenCompra(id_ordencompra=1, producto=producto1, despacho="Santiago")

# Calcular valor final
valor_total = orden1.valor_final()
