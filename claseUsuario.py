# Cree una clase de Python llamada Usuario que use el método init y cree un nombre de usuario y una contraseña. Crea un objeto usando la clase.

class Usuario:
    def __init__(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña

# Crear un objeto de la clase Usuario
usuario1 = Usuario("usuario123", "contraseña123")

# Acceder a los atributos del objeto
print("Nombre de usuario:", usuario1.nombre_usuario)
print("Contraseña:", usuario1.contraseña)

# Output
# Nombre de usuario: usuario123
# Contraseña: contraseña123