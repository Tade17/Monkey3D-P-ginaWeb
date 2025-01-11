class Categoria:
    def __init__(self, id=None, nombre=None, fecha_creacion=None):
        self.id = id
        self.nombre = nombre
        self.fecha_creacion = fecha_creacion

# para depurar
    def __repr__(self):
        return f"Categoria(id={self.id}, nombre='{self.nombre}', fecha_creacion='{self.fecha_creacion}')"

    # Para la serializacion( para las APIs che) broer
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "fecha_creacion": self.fecha_creacion
        }

