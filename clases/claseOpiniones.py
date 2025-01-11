class Opiniones:
    def __init__(self, id=None, resena=None, calificacion=None, fecha_creacion=None, producto_id=None, usuario_id=None):
        self.id = id
        self.resena = resena
        self.calificacion = calificacion
        self.fecha_creacion = fecha_creacion
        self.producto_id = producto_id
        self.usuario_id = usuario_id

    def __repr__(self):
        return f"Opiniones(id={self.id}, resena='{self.resena}', calificacion={self.calificacion}, fecha_creacion='{self.fecha_creacion}', producto_id={self.producto_id}, usuario_id={self.usuario_id})"

    def to_dict(self):
        return {
            "id": self.id,
            "resena": self.resena,
            "calificacion": self.calificacion,
            "fecha_creacion": self.fecha_creacion,
            "producto_id": self.producto_id,
            "usuario_id": self.usuario_id
        }
