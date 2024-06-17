class Producto:
    def __init__(
        self, sku, nombre, categoria, proveedor, stock, valor_neto, impuesto=1.19
    ):
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.proveedor = proveedor
        self.stock = stock
        self.valor_neto = valor_neto
        self.__impuesto = impuesto

    def aumentar_stock(self, cantidad):
        self.stock += cantidad

    def disminuir_stock(self, cantidad):
        if self.stock >= cantidad:
            self.stock -= cantidad
        else:
            print(f"No hay suficiente stock de {self.nombre}")

    def concatenar_nombre_categoria(self):
        return f"{self.nombre} - {self.categoria}"

    def __gt__(self, other):
        return self.valor_neto > other.valor_neto

    def cambiar_proveedor(self, nuevo_proveedor):
        self.proveedor = nuevo_proveedor
