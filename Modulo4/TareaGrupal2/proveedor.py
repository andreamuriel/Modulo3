class Proveedor:
    def __init__(
        self,
        rut,
        nombre_legal,
        razon_social,
        pais,
        tipo_persona,
        fecha_incorporacion=None,
    ):
        self.rut = rut
        self.nombre = nombre_legal
        self.razon_social = razon_social
        self.pais = pais
        self.tipo_persona = tipo_persona
        self.fecha_incorporacion: fecha_incorporacion
        self.inventario_productos = []

    def agregar_producto(self, producto, proveedor):
        if producto.sku in self.inventario_productos:
            return "El producto ya existe en el invantario"
        else:
            self.inventario_productos.append({"sku": producto.nombre, "nombre": producto.nombre, "categoria": producto.categoria, "proveedor": proveedor, "stock": producto.stock, "valor_neto": producto.valor_neto})
            return f"El producto {producto.nombre} fue agregado con exito"


    def eliminar_producto(self, producto_sku):
        for producto in self.inventario_productos:
            if producto_sku in self.inventario_productos:
                self.inventario_productos.remove(producto)
                return f"El producto {producto.nombre} fue eliminado del proveedor"
            else:
                print(f"El producto con SKU {producto_sku} no exite en el inventario")

    def actualizar_stock_producto(self, producto_sku, actualizar_stock):
        for producto in self.inventario_productos:
            if producto_sku == producto.sku:
                producto.stock += actualizar_stock
                return f"El producto {producto.nombre} se actualizo correctamente"
            else:
                print(f"El producto con SKU {producto_sku} no exite en el inventario")


