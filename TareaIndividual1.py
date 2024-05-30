class paciente:
    def __init__(self, nombre, password, correo):
        self.nombre = nombre
        self.password = password
        self.correo = correo

    def datos(self):
        print(f"{self.nombre}")
        print(f"{self.password}")
        print(f"{self.correo}")


class trabajador_salud:
    def __init__(self, nombrepremium, passwordpremium, correopremium):
        self.nombrepremium = nombrepremium
        self.passwordpremium = nombrepremium
        self.correopremium = correopremium

        def datos(self):
            print(f"{self.nombrepremium}")
            print(f"{self.passwordpremium}")
            print(f"{self.correopremium}")

        @property
        def cambiarnombre(self):
            self.nombrepremium = input("Estimado usuario premium, ingrese su nuevo nombre: ")
            return self.nombrepremium 

class master:
    def __init__(self, nombresuperpremium, passwordsuperpremium, correosuperpremium):
        self.nombresuperpremium = nombresuperpremium
        self.passwordsuperpremium = passwordsuperpremium
        self.correosuperpremium = correosuperpremium
    @property
    def playlist(self):
        return 'El usuario superpremium ha cambiado la playlist de spotify'


#Elaborar un programa que recorra una lista con los nombres de







