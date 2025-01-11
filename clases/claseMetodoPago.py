class MetodoPago:
    def __init__(self,id,nombre_metodo_pago,numero_tarjeta,cvv,titular,predeterminado,fecha_vencimiento,fecha_creacion,usuario_id):
        self.id=id
        self.nombre_metodo_pago=nombre_metodo_pago
        self.numero_tarjeta=numero_tarjeta
        self.cvv=cvv
        self.titular=titular
        self.predeterminado=predeterminado
        self.fecha_vencimiento=fecha_vencimiento
        self.fecha_creacion=fecha_creacion
        self.usuario_id=usuario_id

    def __repr__(self):
        return f"MetodoPago (id={self.id}, nombre_metodo_pago={self.nombre_metodo_pago}, numero_tarjeta={self.numero_tarjeta}, cvv={self.cvv},titular={self.titular},predeterminado={self.predeterminado},fecha_vencimiento={self.fecha_vencimiento},fecha_creacion={self.fecha_creacion},usuario_id={self.usuario_id})"
    
    def to_dict(self):
        return{
            "id":self.id,
            "nombre_metodo_pago":self.nombre_metodo_pago,
            "numero_tarjeta":self.numero_tarjeta,
            "cvv":self.cvv,
            "titular":self.titular,
            "predeterminado":self.predeterminado,
            "fecha_vencimiento":self.fecha_vencimiento,
            "fecha_creacion":self.fecha_creacion,
            "usuario_id":self.usuario_id
        }