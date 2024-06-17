class Producto:
    def __init__(
        self,
        sku,
        nombre,
        categoria,
        proveedor,
        stock,
        valor_neto,
        impuesto=1.19,
        fecha_ingreso=None,
    ):
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.proveedor = proveedor
        self.stock = stock
        self.valor_neto = valor_neto
        self.__impuesto = impuesto
        self.fecha_ingreso = fecha_ingreso

    def aumentar_stock(self, cantidad):
        self.stock += cantidad

    def disminuir_stock(self, cantidad):
        if self.stock >= cantidad:
            self.stock -= cantidad
        else:
            print(f"No hay suficiente stock de {self.nombre}")

    def concatenar_nombre_categoria(self):
        return f"{self.nombre} - {self.categoria}"

    def cambiar_proveedor(self, nuevo_proveedor):
        self.proveedor = nuevo_proveedor

    def calcular_impuesto(self, proveedor):
        if proveedor.pais == "chile":
            return self.valor_neto * 0.19
        else:
            return "No corresponde aplicar impuestos"

