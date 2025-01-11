class Direccion:
    def __init__(self, id=None, calle=None, numero_casa=None, referencia=None, fecha_creacion=None, distrito_id=None):
        self.id = id
        self.calle = calle
        self.numero_casa = numero_casa
        self.referencia = referencia
        self.fecha_creacion = fecha_creacion
        self.distrito_id = distrito_id

    def __repr__(self):
        return f"Direccion(id={self.id}, calle='{self.calle}', numero_casa='{self.numero_casa}', referencia='{self.referencia}', fecha_creacion='{self.fecha_creacion}', distrito_id={self.distrito_id})"

    def to_dict(self):
        return {
            "id": self.id,
            "calle": self.calle,
            "numero_casa": self.numero_casa,
            "referencia": self.referencia,
            "fecha_creacion": self.fecha_creacion,
            "distrito_id": self.distrito_id
        }
    