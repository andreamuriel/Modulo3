class Vendedor:
    def __init__(self, rut, nombre, apellido, seccion, comision=0):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.seccion = seccion
        self.__comision = comision

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
