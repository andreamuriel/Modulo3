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

class Producto:
    def __init__(self, sku, nombre, categoria, proveedor, stock, valor_neto, impuesto=1.19):
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.proveedor = proveedor
        self.stock = stock
        self.valor_neto = valor_neto
        self.__impuesto = impuesto

class Vendedor:
    def __init__(self, run, nombre, apellido, seccion, comision=0):
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.seccion = seccion
        self.__comision = comision

def seleccionar_cliente(clientes):
    print("Seleccione un cliente:")
    for i, cliente in enumerate(clientes):
        print(f"{i + 1}. {cliente.nombre} {cliente.apellido}")
    index = int(input("Ingrese el número del cliente: ")) - 1
    if 0 <= index < len(clientes):
        return clientes[index]
    else:
        print("Selección no válida. Intente de nuevo.")
        return seleccionar_cliente(clientes)

def menu():
    print("## Menú Aplicación ##")
    print("Opción 1 - Obtener saldo cliente")
    print("Opción 2 - Agregar saldo cliente")
    opcion = int(input("Ingrese opción elegida: "))

    # Instancias de Clientes
    clientes = [
        Cliente(1, "Andrea", "Venegas", "a.venegas@gmail.com", "15-05-2024", 1000),
        Cliente(2, "Nicolas", "Nuñez", "n.nunez@gmail.com", "15-05-2024", 2000),
        Cliente(3, "Brandon", "Choe", "b.choe@gmail.com", "15-05-2024", 3000),
        Cliente(4, "Elisabeth", "Perez", "e.perez@gmail.com", "15-05-2024", 4000),
        Cliente(5, "Eric", "Venegas", "e.venegas@gmail.com", "15-05-2024", 5000)
    ]

    cliente_seleccionado = seleccionar_cliente(clientes)

    if opcion == 1:
        print(f"El saldo del cliente es: {cliente_seleccionado.saldo}")
    elif opcion == 2:
        monto = float(input("Ingrese el monto a agregar: "))
        cliente_seleccionado.saldo = monto
        print(f"El saldo total de la cuenta es de {cliente_seleccionado.saldo}")
    else:
        print("Opción ingresada no válida")

menu()
