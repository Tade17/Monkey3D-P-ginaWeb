class Producto:
    def __init__(self, id=None, nombre=None, descripcion=None, precio=None, stock=None, imagen=None, fecha_registro=None, estado=1, categoria_id=None):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.imagen = imagen
        self.fecha_registro = fecha_registro
        self.estado = estado
        self.categoria_id = categoria_id

    def __repr__(self):
        return f"Producto(id={self.id}, nombre='{self.nombre}', descripcion='{self.descripcion}', precio={self.precio}, stock={self.stock}, imagen='{self.imagen}', fecha_registro='{self.fecha_registro}', estado={self.estado}, categoria_id={self.categoria_id})"

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "stock": self.stock,
            "imagen": self.imagen,
            "fecha_registro": self.fecha_registro,
            "estado": self.estado,
            "categoria_id": self.categoria_id
        }
