
# Primer nivel
class Cliente:
    def __init__(self, rut, nombre, apellido):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido

    def info(self):
        pass

# Segundo nivel


class Persona(Cliente):
    def info(self):
        print("Accediendo a informacion de cliente tipo Persona Natural")
        print(f"Nombre Cliente : {self.nombre} \n")


class Empresa(Cliente):
    def __init__(self, rut, nombre, apellido, nombre_empresa):
        super().__init__(rut, nombre, apellido)
        self.nombre_empresa = nombre_empresa

    def info(self):
        print("Accediendo a cliente de tipo Empresa")
        print(f"Nombre Cliente: {self.nombre}")
        print(f"Nombre Empresa: {self.nombre_empresa} \n")

# Tercer nivel


class Pyme(Empresa):
    def info(self):
        print("Accediendo a informacion Pyme")
        print(f"Nombre Cliente: {self.nombre}")
        print(f"Nombre Empresa: {self.nombre_empresa} \n")


# Creando Cliente tipo persona y llamando su metodo info
persona1 = Persona("13445767-K", "Vanesa", "Jimenez")
persona1.info()

# Creando cliente tipo empresa y llamando a su metodo info
empresa1 = Empresa("11433476-5", "Antonio", "Rios", "Camanchaca")
empresa1.info()

# Accediendo a informacion pyme
pyme1 = Pyme("15787699-0", "Juan", "Altamirano", "Donde la Vecina")
pyme1.info()
