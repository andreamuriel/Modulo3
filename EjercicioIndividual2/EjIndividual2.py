# Módulo 3: Actividad Individual 2
# Alumna: Andrea Venegas

# ● En base al contexto: Piensa en una aplicación web que busque solucionar una problemática.
print()
print('ʕ·ᴥ·ʔ Bienvenido a la aplicación que solucionará todos tus problemas ʕ·ᴥ·ʔ')
print()
# ● Esta aplicación debe entregar la posibilidad de iniciar sesión con un perfil individual.


# ● ¿Qué problemas pueden surgir si otra persona quiere buscar a un usuario e ingresa
# manualmente su nombre? ¿Cómo solucionarías este problema?

# Un problema que puede surgir es que la coincidencia no sea exacta, por ejemplo el uso de mayúscula al inicio o que solo use minúsculas, para solucionarlo se puede usar el comando ".capitalize()" o ".lower()" al buscar un elemento de la lista para cambiar su primera letra a mayúscula o cambiar todas las letras en minúsculas, respectivamente.

# ● Generalmente, uno ingresa a su cuenta personal en una página, ésta te saluda y te reconoce
# ● Intentemos replicar esto. Crea un string con el nombre de al menos 7 usuarios de tu aplicación.

# lista = ['Andrea', 'Ignacio', 'Nicolás', 'Daniela', 'Johana', 'Alan', 'Tomas']

# peticion = input('Ingrese el nombre que desea buscar: ').capitalize() #.lower() para que todas las letras sean en minuscula

# if peticion in lista:
#     print(True)
# else:
#     print(False)

# ● Ahora piensa en tres de ellos. Buscalos en la lista con el método adecuado.

lista = ['Andrea', 'Ignacio', 'Nicolás', 'Daniela', 'Johana', 'Alan', 'Tomas']
names = [nombre.lower() for nombre in lista]
# print(names)

peticion = input('Ingrese 3 nombres de Usuario separados por un espacio: ').lower()
print()
if " " in peticion:
    peticion = peticion.split(" ")
else:
    # ● Convierte tu string en una lista, en la cual cada elemento es un usuario.
    peticion = [peticion]
for nombre in peticion:
    if nombre in names: print(f'{nombre.capitalize()} está en la lista. Bienvenido/a {nombre.capitalize()}') 
    else: print(f'{nombre.capitalize()} no está en la lista') 
print()
# ● Imprime en pantalla la cantidad usuarios que tiene tu aplicación.
    
print(f'La cantidad de usuarios de la aplicación son: {len(lista)}')
print()
# ● Imprime en pantalla un mensaje de saludo a los diferentes usuarios. ¿Qué técnica puedes utilizar para realizar esto?
# Para saludar a todos los usuarios se puede usar un ciclo for para buscar cada elemento de la lista que en este caso son los nombres de usuario y con un print escribirle el mensahe de saludo: 
 
for nombre in lista:
    print(f'Bienvenido/a: {nombre}')

#Para saludar solo a los nombres ingresados que están en la lista se agregó el mensaje "Bienvenida/o {nombre.capitalize()}" dentro del print de la línea 42.


 






#ignorar esto por favor:

#Otras formas de escribir lo mismo: 
# lista = ['Andrea', 'Ignacio', 'Nicolás', 'Daniela', 'Johana', 'Alan', 'Tomas']
# lista_minus = []
# for nombre in lista:
#     lista_minus.append(nombre.lower())

# print(lista_minus)
# print('----------------------')

# for index in range(len(lista)):
#     lista[index] = lista[index].lower()

# print(lista)
# print('----------------------')

# names = [nombre.lower() for nombre in lista]
# print(names)
