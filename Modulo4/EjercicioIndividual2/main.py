from package.cliente import Cliente
from package.producto import Producto
from package.vendedor import Vendedor
from package.compra import Compra

# Creacion de instancias de Clientes

cliente_1 = Cliente(1, "Andrea", "Venegas", "a.venegas@gmail.com", "15-05-2024", 1000)
cliente_2 = Cliente(1, "Nicolas", "Nuñez", "n.nunez@gmail.com", "15-05-2024", 2000)
cliente_3 = Cliente(1, "Brandon", "Choe", "b.choe@gmail.com", "15-05-2024", 3000)
cliente_4 = Cliente(1, "Elisabeth", "Perez", "e.perez@gmail.com", "15-05-2024", 4000)
cliente_5 = Cliente(1, "Eric", "Venegas", "e.venegas@gmail.com", "15-05-2024", 5000)

# Creacion de instancias de Productos
producto_1 = Producto(
    sku="rr333",
    nombre="Camiseta",
    categoria="Ropa",
    proveedor="Adidas",
    stock=100,
    valor_neto=10000,
)
producto_2 = Producto(
    sku="bb456",
    nombre="Pantalon",
    categoria="Ropa",
    proveedor="Nike",
    stock=34,
    valor_neto=34000,
)
producto_3 = Producto(
    sku="hh778",
    nombre="Short",
    categoria="Ropa",
    proveedor="Under Armour",
    stock=50,
    valor_neto=15000,
)
producto_4 = Producto(
    sku="aa332",
    nombre="Zapatilla",
    categoria="Ropa",
    proveedor="Under Armour",
    stock=20,
    valor_neto=69000,
)
producto_5 = Producto(
    sku="jj345",
    nombre="Jockey",
    categoria="Ropa",
    proveedor="Ellese",
    stock=30,
    valor_neto=18000,
)
# Creacion instancias de Vendedores
vendedor_1 = Vendedor(
    run="15567904-9",
    nombre="Hugo",
    apellido="Caballero",
    seccion="Ventas",
    comision=0.1,
)
vendedor_2 = Vendedor(
    run="123453423-9",
    nombre="Alan",
    apellido="Muñoz",
    seccion="Ventas",
    comision=0.15,
)
vendedor_3 = Vendedor(
    run="17456778-9",
    nombre="Daniel",
    apellido="Farias",
    seccion="Ventas",
    comision=0.1,
)
vendedor_4 = Vendedor(
    run="14561223-9",
    nombre="Marco",
    apellido="Diaz",
    seccion="Ventas",
    comision=0.1,
)
vendedor_5 = Vendedor(
    run="13223778-9",
    nombre="Bastian",
    apellido="SanMartin",
    seccion="Ventas",
    comision=0.15,
)


def menu():
    print("## Menu Aplicacion ##")
    print("Opcion 1 - Obtener saldo cliente")
    print("Opcion 2 - Agregar saldo cliente")
    opcion = int(input("Ingrese opcion elegida : "))

    if opcion == 1:
        print(f"El saldo del cliente es : {cliente_1.saldo}")
    elif opcion == 2:
        cliente_1.saldo = 3000
        print(f"El saldo total de la cuenta es de {cliente_1.saldo}")
    else:
        print("Opcion ingresada no valida")


menu()