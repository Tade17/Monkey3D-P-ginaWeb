class Usuario:
    def __init__(self, id=None, nombre=None, apellidos=None, email=None, contrasena=None, rol=None, foto=None, telefono=None, activo=1, fecha_registro=None):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.contrasena = contrasena
        self.rol = rol
        self.foto = foto
        self.telefono = telefono
        self.activo = activo
        self.fecha_registro = fecha_registro

    def __repr__(self):
        return f"Usuario(id={self.id}, nombre='{self.nombre}', apellidos='{self.apellidos}', email='{self.email}', rol='{self.rol}', foto='{self.foto}', telefono='{self.telefono}', activo={self.activo}, fecha_registro='{self.fecha_registro}')"

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellidos": self.apellidos,
            "email": self.email,
            "rol": self.rol,
            "foto": self.foto,
            "telefono": self.telefono,
            "activo": self.activo,
            "fecha_registro": self.fecha_registro
        }
