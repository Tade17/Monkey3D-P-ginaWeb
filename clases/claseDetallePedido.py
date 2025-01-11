class Detalle_pedido:
    def __init__(self, id=None, precioUnitario=None, cantidad=None, fecha_creacion=None, producto_id=None, pedido_id=None):
        self.id = id
        self.precioUnitario = precioUnitario
        self.cantidad = cantidad
        self.fecha_creacion = fecha_creacion
        self.producto_id = producto_id
        self.pedido_id = pedido_id

    def __repr__(self):
        return f"Detalle_pedido(id={self.id}, precioUnitario={self.precioUnitario}, cantidad={self.cantidad}, fecha_creacion='{self.fecha_creacion}', producto_id={self.producto_id}, pedido_id={self.pedido_id})"

    def to_dict(self):
        return {
            "id": self.id,
            "precioUnitario": self.precioUnitario,
            "cantidad": self.cantidad,
            "fecha_creacion": self.fecha_creacion,
            "producto_id": self.producto_id,
            "pedido_id": self.pedido_id
        }