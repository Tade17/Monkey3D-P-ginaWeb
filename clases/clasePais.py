class Pais:
    def __init__(self,id,nombre,codigo_iso,disponible,fecha_creacion):
        self.id=id
        self.nombre=nombre
        self.codigo_iso=codigo_iso
        self.disponible=disponible
        self.fecha_creacion=fecha_creacion

    def __repr__(self):
        return f"Pais(id={self.id}, nombre='{self.nombre}',codigo_iso='{self.codigo_iso}', disponible={self.disponible}, fecha_creacion='{self.fecha_creacion}')"
    def to_dict(self):
         return {
            "id": self.id,
            "nombre": self.nombre,
            "codigo_iso": self.codigo_iso,
            "disponible": self.disponible,
            "fecha_creacion": self.fecha_creacion,
            }