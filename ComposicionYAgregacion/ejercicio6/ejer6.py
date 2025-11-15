class Producto:
    def __init__(self, idProducto: str, nombre: str):
        self.idProducto = idProducto
        self.nombre = nombre

class Servicio(Producto):
    def __init__(self, idProducto: str, nombre: str, duracion: int, esRecurrente: bool):
        super().__init__(idProducto, nombre)
        self.duracion = duracion
        self.esRecurrente = esRecurrente

class Medicamento(Producto):
    def __init__(self, idProducto: str, nombre: str, laboratorio: str, requiereReceta: bool):
        super().__init__(idProducto, nombre)
        self.laboratorio = laboratorio
        self.requiereReceta = requiereReceta

class DetallePedido:
    def __init__(self, producto: Producto, cantidad: int, subtotal: float):
        self.producto = producto
        self.cantidad = cantidad
        self.subtotal = subtotal

class Registro:
    def __init__(self, idPedido: str, fecha: str):
        self.idPedido = idPedido
        self.fecha = fecha
        self.detalles = []