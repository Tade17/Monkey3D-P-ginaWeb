class Pago:
    def __init__(self, id=None, fecha=None, monto=None, estado=None, metodo_pago=None, pedido_id=None):
        self.id = id
        self.fecha = fecha
        self.monto = monto
        self.estado = estado
        self.metodo_pago = metodo_pago
        self.pedido_id = pedido_id

    def __repr__(self):
        return f"Pago(id={self.id}, fecha='{self.fecha}', monto={self.monto}, estado='{self.estado}', metodo_pago='{self.metodo_pago}', pedido_id={self.pedido_id})"

    def to_dict(self):
        return {
            "id": self.id,
            "fecha": self.fecha,
            "monto": self.monto,
            "estado": self.estado,
            "metodo_pago": self.metodo_pago,
            "pedido_id": self.pedido_id
        }
