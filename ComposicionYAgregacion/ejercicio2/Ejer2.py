class Empleado:
    def __init__(self, nombre, cargo, sueldo):
        self.nombre = nombre
        self.cargo = cargo
        self.sueldo = sueldo

    def __str__(self):
        return f"{self.nombre} / {self.cargo} / bs {self.sueldo}"


class Departamento:
    def __init__(self, nombre, area):
        self.nombre = nombre
        self.area = area
        self.empleados = []   

    def agregarEmpleado(self, emp):
        
        self.empleados.append(emp)




    def mostrarEmpleados(self):
        print(f"\n-- {self.nombre} ({self.area}) --")
        if len(self.empleados) == 0:
            print("no ay empleados")
        
        else:
            for emp in self.empleados:
                print("  *", emp)

    
    
    
    def cambioSalario(self, porc):
   
        for emp in self.empleados:
            nuevo = emp.sueldo + emp.sueldo * (porc / 100)
            emp.sueldo = round(nuevo, 2)

    def pertenece(self, emp):
        return emp in self.empleados





#main

# 1.
dep1 = Departamento("departamento 1", "informatica")
dep2 = Departamento("departamento 2", "marketing")

# empleados **
empleados_dep1 = [
    Empleado("juana", "ingeniero", 3000),
    Empleado("luis", "desarrollador", 3200),
    Empleado("maria", "analista", 2500),
    Empleado("carlos", "administrador", 4000),
    Empleado("carla", "especialista", 6000)
]


for e in empleados_dep1:
    dep1.agregarEmpleado(e)


dep1.mostrarEmpleados()
dep2.mostrarEmpleados()

# cambio de sal
dep1.cambioSalario(10)
print("\nsalarios cambios")
dep1.mostrarEmpleados()

#revision
for e in dep1.empleados:
    if dep2.pertenece(e):
        print(e.nombre, "esta tambien en dep2 (raro)")
    else:
        print(e.nombre, "solo está en dep1")

# moverr
print("\nmoviendo empleados del departamento 1 a 2\n")
for e in dep1.empleados:
    dep2.agregarEmpleado(e)


dep1.empleados = []


dep1.mostrarEmpleados()
dep2.mostrarEmpleados()
