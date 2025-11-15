class Doctor:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
    
    def mostrar_info(self):
        return f"dr. {self.nombre} - {self.especialidad}"

class Hospital:
    def __init__(self, nombre):
        self.nombre = nombre
        self.doctores = []
    
    def agregar_doctor(self, doctor):
        self.doctores.append(doctor)
        print(f"doctor {doctor.nombre} agregado al hospital {self.nombre}")
    
    def mostrar_doctores(self):
        print(f"\n--- doctores del hospital {self.nombre} ---")
        if len(self.doctores) == 0:
            print("no hay doctores en este hospital")
        else:
            for i, doctor in enumerate(self.doctores, 1):
                print(f"{i}. {doctor.mostrar_info()}")

#crear doc
print("creando doctores...")
doctor1 = Doctor("juan carlos mendoza", "cardiologia")
doctor2 = Doctor("ana maria torres", "pediatria")
doctor3 = Doctor("luis alberto garcia", "cirugia")
doctor4 = Doctor("maria elena lopez", "ginecologia")
doctor5 = Doctor("carlos perez", "traumatologia")

#crear hosp
print("creando hospitales...")
hospital1 = Hospital("hospital san juan de dios")
hospital2 = Hospital("hospital obrero")
hospital3 = Hospital("hospital del niño")

#asignar
print("\nasignando doctores a hospitales...")

#hos1
hospital1.agregar_doctor(doctor1)
hospital1.agregar_doctor(doctor2)
hospital1.agregar_doctor(doctor3)

#hos2
hospital2.agregar_doctor(doctor2)
hospital2.agregar_doctor(doctor4)
hospital2.agregar_doctor(doctor5)

#hos3
hospital3.agregar_doctor(doctor1)
hospital3.agregar_doctor(doctor3)
hospital3.agregar_doctor(doctor5)


hospital1.mostrar_doctores()
hospital2.mostrar_doctores()
hospital3.mostrar_doctores()


print("\n--- informacion de cada doctor ---")
doctores = [doctor1, doctor2, doctor3, doctor4, doctor5]

for doctor in doctores:
    print(f"\ndr. {doctor.nombre} trabaja en:")
    trabajos = 0
    for hospital in [hospital1, hospital2, hospital3]:
        if doctor in hospital.doctores:
            print(f" - {hospital.nombre}")
            trabajos += 1
    if trabajos == 0:
        print(" no trabaja en ningun hospital")