class Administrator:
    def __init__(self, username, email, rol_permission):
        self.username = username
        self.email = email
        self.rol_permission = rol_permission

    def create_new_users():
        print("Creacion de nuevos usuarios")

    def assign_rol_permission():
        print("Asignar roles sa usuarios")

    def sensible_data_access():
        print("Acceder a data sensible de la empresa")


class Client:
    def __init__(self, username, email, rol_permission):
        self.username = username
        self.email = email
        self.rol_permission = rol_permission

    def watch_products():
        print("Ver productos tienda")

    def buy_products():
        print("Comprar productos de la tienda")

    def history_buy_products():
        print("Ver historial de compras")

    def product_review():
        print("Reseña de producto")


class Seller:
    def __init__(self, username, email, rol_permission):
        self.username = username
        self.email = email
        self.rol_permission = rol_permission

    def sales_commission():
        print("Comisiones por ventas")

    def sales_history():
        print("Historial de ventas")

    def product_modify():
        print("Modificar producto en su precio, descripcion o stock")

    def add_product():
        print("Agregar nuevo producto")