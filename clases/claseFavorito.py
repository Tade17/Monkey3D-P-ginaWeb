class Favorito:
    def __init__(self,id,fecha_creacion,producto_id,usuario_id):
        self.id=id
        self.fecha_creacion=fecha_creacion
        self.producto_id=producto_id
        self.usuario_id=usuario_id
    
    def __repr__(self):
        return f"Favorito( id ={self.id},fecha_creacion='{self.fecha_creacion}',producto_id={self.producto_id},usuario_id={self.usuario_id})"
    
    def to_dict(self):
        return{
            "id":self.id,
            "fecha_creacion":self.fecha_creacion,
            "producto_id":self.producto_id,
            "usuario_id":self.usuario_id
        }