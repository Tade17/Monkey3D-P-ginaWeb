class Distrito:
    def __init__(self, id=None, nombre=None, disponible=1, fecha_creacion=None, provincia_id=None, codigo_postal=None):
        self.id = id
        self.nombre = nombre
        self.disponible = disponible
        self.fecha_creacion = fecha_creacion
        self.provincia_id = provincia_id
        self.codigo_postal = codigo_postal

    def __repr__(self):
        return f"Distrito(id={self.id}, nombre='{self.nombre}', disponible={self.disponible}, fecha_creacion='{self.fecha_creacion}', provincia_id={self.provincia_id}, codigo_postal='{self.codigo_postal}')"

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "disponible": self.disponible,
            "fecha_creacion": self.fecha_creacion,
            "provincia_id": self.provincia_id,
            "codigo_postal": self.codigo_postal
        }