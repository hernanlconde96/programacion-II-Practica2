class Ropa:
    def __init__(self, tipo, material):
        self.tipo = tipo
        self.material = material

    def __str__(self):
        return f"{self.tipo} - {self.material}"


class Ropero:
    def __init__(self, material):
        self.material = material
        self.ropas = []   
        self.nroRopas = 0




    def adicionarRopa(self, ropa):
       
        if self.nroRopas < 20:
            self.ropas.append(ropa)
            self.nroRopas += 1
        else:
            print("ropero lleno")


    def eliminarPorMaterial(self, mat):
      

        self.ropas = [r for r in self.ropas if r.material != mat]
        self.nroRopas = len(self.ropas)

    def eliminarPorTipo(self, tipo):
        self.ropas = [r for r in self.ropas if r.tipo != tipo]
        self.nroRopas = len(self.ropas)

    def mostrarPorMaterial(self, mat):
        print(f"\nprenda de material: '{mat}':")
        for r in self.ropas:
            if r.material == mat:
                print(" *", r)

    def mostrarPorTipo(self, tipo):
        print(f"\nprndas de tipo: '{tipo}':")
        for r in self.ropas:
            if r.tipo == tipo:
                print(" *", r)















rop = Ropero("metal")


n = int(input("numero de prendas a agregar? "))

for i in range(n):
    print("\nprenda", i+1)
    t = input("tipo: ")
    m = input("material: ")
    nueva = Ropa(t, m)
    rop.adicionarRopa(nueva)


print("\nropero actual:")
for r in rop.ropas:
    print(" *", r)


mat_x = input("\nmaterial que va eliminar*** ")
rop.eliminarPorMaterial(mat_x)


tipo_x = input("tipo que va eliminar*** ")
rop.eliminarPorTipo(tipo_x)


mat_buscar = input("\nmaterial que va mostrar*** ")
rop.mostrarPorMaterial(mat_buscar)

tipo_buscar = input("tipo a mostrar*** ")
rop.mostrarPorTipo(tipo_buscar)
