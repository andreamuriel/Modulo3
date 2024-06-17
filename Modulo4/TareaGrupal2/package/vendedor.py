class Vendedor:
    def __init__(
        self, rut, nombre, apellido, seccion, comision=0, fecha_incorporacion=None
    ):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.seccion = seccion
        self.__comision = comision
        self.fecha_incorporacion = fecha_incorporacion

    def aumentar_comision(self, cantidad):
        self.__comision += cantidad

    def disminuir_comision(self, cantidad):
        if self.__comision >= cantidad:
            self.__comision -= cantidad
        else:
            print("La comisión no puede ser menor a 0")

    def concatenar_nombre_apellido(self):
        return f"{self.nombre} {self.apellido}"

    def cambiar_apellido(self, nuevo_apellido):
        self.apellido = nuevo_apellido

    def vender(self, vendedor, producto, cliente):
        if producto.stock < 0:
            return "El producto no tiene stock suficiente"
        else:
            producto.stock -= 1
            return f"El producto {producto.nombre} descontado correctamente de {producto.nombre}"

        comision_vendedor = producto.valor_neto * 0.005
        self.__comision += comision_vendedor

        if cliente.saldo < producto.valor_neto:
            return "Cliente no tiene saldo suficiente para comprar producto"
        else:
            total_a_pago = producto.valor_neto * 1.019 + comision_vendedor
            cliente.saldo -= total__a_pago
            print(f"Total a pagar con IVA: {total_a_pago}")

