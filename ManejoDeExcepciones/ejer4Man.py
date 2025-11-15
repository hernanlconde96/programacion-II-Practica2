class ProductoNoEncontradoException(Exception):
    pass

class StockInsuficienteException(Exception):
    pass

class CodigoDuplicadoException(Exception):
    pass

class ValorNegativoException(Exception):
    pass

class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def mostrar_info(self):
        return f"codigo: {self.codigo}, nombre: {self.nombre}, precio: {self.precio}, stock: {self.stock}"

class Inventario:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, producto):
        for p in self.productos:
            if p.codigo == producto.codigo:
                raise CodigoDuplicadoException(f"el codigo {producto.codigo} ya existe")
        
        if producto.precio < 0:
            raise ValorNegativoException("el precio no puede ser negativo")
        
        if producto.stock < 0:
            raise ValorNegativoException("el stock no puede ser negativo")
        
        self.productos.append(producto)
        print(f"producto {producto.nombre} agregado correctamente")
    
    def buscar_producto(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        
        raise ProductoNoEncontradoException(f"producto con codigo {codigo} no encontrado")
    
    def vender_producto(self, codigo, cantidad):
        producto = self.buscar_producto(codigo)
        
        if producto.stock < cantidad:
            raise StockInsuficienteException(f"stock insuficiente. hay {producto.stock} unidades, se pidieron {cantidad}")
        
        producto.stock -= cantidad
        total = producto.precio * cantidad
        print(f"venta realizada: {cantidad} unidades de {producto.nombre}")
        print(f"total: {total}")
        print(f"stock restante: {producto.stock}")

print("sistema de inventario")

inventario = Inventario()

try:
    p1 = Producto("001", "laptop", 1500, 10)
    p2 = Producto("002", "mouse", 25, 50)
    p3 = Producto("003", "teclado", 45, 30)
    
    inventario.agregar_producto(p1)
    inventario.agregar_producto(p2)
    inventario.agregar_producto(p3)
    
except (CodigoDuplicadoException, ValorNegativoException) as e:
    print(f"error: {e}")

print("\n--- probando busqueda ---")
try:
    producto = inventario.buscar_producto("001")
    print(f"encontrado: {producto.mostrar_info()}")
    
    producto = inventario.buscar_producto("999")
    print(f"encontrado: {producto.mostrar_info()}")
    
except ProductoNoEncontradoException as e:
    print(f"error: {e}")

print("\n--- probando ventas ---")
try:
    inventario.vender_producto("001", 2)
    inventario.vender_producto("002", 60)
    
except (ProductoNoEncontradoException, StockInsuficienteException) as e:
    print(f"error: {e}")

print("\n--- probando agregar con errores ---")
try:
    p4 = Producto("001", "tablet", 300, 5)
    inventario.agregar_producto(p4)
    
except (CodigoDuplicadoException, ValorNegativoException) as e:
    print(f"error: {e}")

try:
    p5 = Producto("004", "monitor", -100, 5)
    inventario.agregar_producto(p5)
    
except (CodigoDuplicadoException, ValorNegativoException) as e:
    print(f"error: {e}")

try:
    p6 = Producto("005", "audifonos", 50, -2)
    inventario.agregar_producto(p6)
    
except (CodigoDuplicadoException, ValorNegativoException) as e:
    print(f"error: {e}")