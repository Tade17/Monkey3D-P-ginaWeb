class Pedido:
    def __init__(self, id=None, fecha_pedido=None, total=None, estado=None, domicilio_id=None, usuario_id=None):
        self.id = id
        self.fecha_pedido = fecha_pedido
        self.total = total
        self.estado = estado
        self.domicilio_id = domicilio_id
        self.usuario_id = usuario_id

    def __repr__(self):
        return f"Pedido(id={self.id}, fecha_pedido='{self.fecha_pedido}', total={self.total}, estado='{self.estado}', domicilio_id={self.domicilio_id}, usuario_id={self.usuario_id})"

    def to_dict(self):
        return {
            "id": self.id,
            "fecha_pedido": self.fecha_pedido,
            "total": self.total,
            "estado": self.estado,
            "domicilio_id": self.domicilio_id,
            "usuario_id": self.usuario_id
        }
