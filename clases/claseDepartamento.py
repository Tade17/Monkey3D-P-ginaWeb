class Departamento:
    def __init__(self, id=None, nombre=None, codigo_postal=None, disponible=1, fecha_creacion=None):
        self.id = id
        self.nombre = nombre
        self.codigo_postal = codigo_postal
        self.disponible = disponible
        self.fecha_creacion = fecha_creacion

    def __repr__(self):
        return f"Departamento(id={self.id}, nombre='{self.nombre}', codigo_postal='{self.codigo_postal}', disponible={self.disponible}, fecha_creacion='{self.fecha_creacion}')"

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "codigo_postal": self.codigo_postal,
            "disponible": self.disponible,
            "fecha_creacion": self.fecha_creacion
        }