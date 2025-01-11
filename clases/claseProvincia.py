class Provincia:
    def __init__(self, id=None, nombre=None, disponible=1, fecha_creacion=None, departamento_id=None, codigo_postal=None):
        self.id = id
        self.nombre = nombre
        self.disponible = disponible
        self.fecha_creacion = fecha_creacion
        self.departamento_id = departamento_id
        self.codigo_postal = codigo_postal

    def __repr__(self):
        return f"Provincia(id={self.id}, nombre='{self.nombre}', disponible={self.disponible}, fecha_creacion='{self.fecha_creacion}', departamento_id={self.departamento_id}, codigo_postal='{self.codigo_postal}')"

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "disponible": self.disponible,
            "fecha_creacion": self.fecha_creacion,
            "departamento_id": self.departamento_id,
            "codigo_postal": self.codigo_postal
        }