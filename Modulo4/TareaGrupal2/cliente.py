class Cliente:
    def __init__(
        self, id_cliente, nombre, apellido, correo, fecha_registro, saldo, edad=None
    ):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.fecha_registro = fecha_registro
        self.__saldo = saldo
        self.edad = edad
        self.clientes = []

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, agrega_saldo):
        self.__saldo += agrega_saldo
        return self.__saldo

    def descontar_saldo(self, cantidad):
        if self.__saldo >= cantidad:
            self.__saldo -= cantidad
        else:
            print("Saldo insuficiente")

    def actualizar_correo(self, nuevo_correo):
        self.correo = nuevo_correo

    def crear_cliente(self,id_cliente, nombre, apellido, correo, fecha_registro, saldo, edad ):
        self.clientes.append({"id_cliente": id_cliente, "nombre": nombre, "apellido": apellido, "correo": correo, "fecha_registro": fecha_registro, "saldo": saldo, "edad": edad})
        return print("Cliente creado correctamente")