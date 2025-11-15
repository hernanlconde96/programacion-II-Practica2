class Persona:
    def __init__(self, nombre, edad, ci):
        self.nombre = nombre
        self.edad = edad
        self.ci = ci
        self.fraternidad = None
        self.facultad = None
    
    def mostrar(self):
        return f"{self.nombre} - {self.edad} anios - ci: {self.ci}"

class Facultad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.bailarines = []
    
    def agregar_bailarin(self, bailarin):
        if bailarin not in self.bailarines:
            self.bailarines.append(bailarin)
            bailarin.facultad = self

class Fraternidad:
    def __init__(self, nombre, encargado):
        self.nombre = nombre
        self.encargado = encargado
        self.bailarines = []
        encargado.fraternidad = self
    
    def agregar_bailarin(self, bailarin):
        if bailarin.fraternidad and bailarin.fraternidad != self:
            print(f"error: {bailarin.nombre} ya esta en otra fraternidad")
            return False
        
        if bailarin not in self.bailarines:
            self.bailarines.append(bailarin)
            bailarin.fraternidad = self
            return True
        return False

class Sistema:
    def __init__(self):
        self.fraternidades = []
        self.facultades = []
        self.bailarines = []
    
    def registrar(self, nombre, edad, ci, facultad, fraternidad):
        for b in self.bailarines:
            if b.ci == ci:
                print(f"ya existe bailarin su ci: {ci}")
                return None
        
        nuevo = Persona(nombre, edad, ci)
        facultad.agregar_bailarin(nuevo)
        
        if not fraternidad.agregar_bailarin(nuevo):
            return None
        
        self.bailarines.append(nuevo)
        print(f"registrado: {nombre} en {fraternidad.nombre}")
        return nuevo
    
    def mostrar_todos(self):
        print("\n--- todos los bailarines ---")
        for b in self.bailarines:
            frat = b.fraternidad.nombre if b.fraternidad else "sin fraternidad"
            fac = b.facultad.nombre if b.facultad else "sin facultad"
            print(f"{b.nombre} ** {frat} ** {fac}")
    
    
    
    
    def mostrar_fraternidad(self, frat):
        print(f"\n--- {frat.nombre} ---")
        print(f"encargado: {frat.encargado.nombre}")
        for b in frat.bailarines:
            print(f" - {b.nombre} ({b.facultad.nombre})")
    
    
    
    def mostrar_facultad(self, fac):
        print(f"\n--- {fac.nombre} ---")
        for b in fac.bailarines:
            frat = b.fraternidad.nombre if b.fraternidad else "sin fraternidad"
            print(f" - {b.nombre} ({frat})")
    
    
    
    
    def verificar_duplicados(self):
        print("\n--- verificar duplicados ---")
        cis = []
        for b in self.bailarines:
            if b.ci in cis:
                print(f"duplicado encontrado: {b.nombre} - CI: {b.ci}")
                return
            cis.append(b.ci)
        print("no hay duplicados")
    
    
    
    
    def info_edades(self):
        if self.bailarines:
            edades = [b.edad for b in self.bailarines]
            print(f"\n--- info edades ---")
            print(f"promedio: {sum(edades)/len(edades):.1f} años")
            print(f"minima: {min(edades)} años")
            print(f"maxima: {max(edades)} años")






sistema = Sistema()

#facultad
fac1 = Facultad("facultad de informatica")
fac2 = Facultad("facultad de economia")
sistema.facultades = [fac1, fac2]

#encargad

enc1 = Persona("carlos Mendoza", 25, "1234567")
enc2 = Persona("maria Torres", 24, "7654321")

#frater
print("creando fraternidades...")
frat1 = Fraternidad("los dragones", enc1)
frat2 = Fraternidad("los halcones", enc2)
sistema.fraternidades = [frat1, frat2]

#reg bailarin
print("\nregistrando bailarines...")

#frat1
sistema.registrar("fernando perez", 20, "1111111", fac1, frat1)
sistema.registrar("carla lopez", 21, "2222222", fac1, frat1)
sistema.registrar("max garcua", 22, "3333333", fac2, frat1)

#frat2
sistema.registrar("juana martinez", 19, "4444444", fac2, frat2)
sistema.registrar("diego silva", 23, "5555555", fac1, frat2)

#dupli
print("\nintento de duplicado")
sistema.registrar("falso nombre", 20, "1111111", fac1, frat1)

#cambio
print("\nintento cambiar fraternidad")
sistema.registrar("juan perez", 20, "1111111", fac1, frat2)


sistema.mostrar_todos()
sistema.mostrar_fraternidad(frat1)
sistema.mostrar_fraternidad(frat2)
sistema.mostrar_facultad(fac1)
sistema.mostrar_facultad(fac2)

#ver
sistema.verificar_duplicados()
sistema.info_edades()