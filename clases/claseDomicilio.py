class Domicilio:
    def __init__(self, id=None, predeterminado=None, fecha_creacion=None, direccion_id=None, usuario_id=None):
        self.id = id
        self.predeterminado = predeterminado
        self.fecha_creacion = fecha_creacion
        self.direccion_id = direccion_id
        self.usuario_id = usuario_id

    def __repr__(self):
        return f"Domicilio(id={self.id}, predeterminado={self.predeterminado}, fecha_creacion='{self.fecha_creacion}', direccion_id={self.direccion_id}, usuario_id={self.usuario_id})"

    def to_dict(self):
        return {
            "id": self.id,
            "predeterminado": self.predeterminado,
            "fecha_creacion": self.fecha_creacion,
            "direccion_id": self.direccion_id,
            "usuario_id": self.usuario_id
        }