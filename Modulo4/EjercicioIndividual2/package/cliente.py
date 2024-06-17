class Cliente:
    def __init__(self, id_cliente, nombre, apellido, correo, fecha_registro, saldo):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.fecha_registro = fecha_registro
        self.__saldo = saldo

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
