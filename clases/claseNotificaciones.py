class Notificaciones:
    def __init__(self,id,tipo,visto,fecha_creacion,usuario_id,pedido_id):
        self.id=id
        self.tipo=tipo
        self.visto=visto
        self.fecha_creacion=fecha_creacion
        self.usuario_id=usuario_id
        self.pedido_id=pedido_id
    def __repr__(self):
        return f"Notificaciones(id={self.id}, tipo='{self.tipo}', visto={self.visto}, fecha_creacion='{self.fecha_creacion}',usuario_id={self.usuario_id}, pedido_id={self.pedido_id})"
    
    def to_dict(self):
        return{
            "id": self.id,
            "tipo": self.tipo,
            "visto": self.visto,
            "fecha_creacion": self.fecha_creacion,
            "usuario_id": self.usuario_id,
            "pedido_id": self.pedido_id
        }