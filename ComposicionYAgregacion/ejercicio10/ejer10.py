class Persona:
    def __init__(self, nombre, apellido, edad, ci):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ci = ci
    
    def mostrar_info(self):
        return f"{self.nombre} {self.apellido} - {self.edad} años - ci: {self.ci}"

class Speaker(Persona):
    def __init__(self, nombre, apellido, edad, ci, especialidad):
        super().__init__(nombre, apellido, edad, ci)
        self.especialidad = especialidad

class Charla:
    def __init__(self, lugar, nombre_charla, speaker):
        self.lugar = lugar
        self.nombre_charla = nombre_charla
        self.speaker = speaker
        self.np = 0
        self.participantes = []
    
    def agregar_participante(self, participante):
        if self.np < 50:
            self.participantes.append(participante)
            self.np += 1
            return True
        return False

class Evento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nc = 0
        self.charlas = []
    
    def agregar_charla(self, charla):
        if self.nc < 50:
            self.charlas.append(charla)
            self.nc += 1
            return True
        return False
    
    def edad_promedio_participantes(self):
        if self.nc == 0:
            return 0
        
        todas_edades = []
        for charla in self.charlas:
            for participante in charla.participantes:
                todas_edades.append(participante.edad)
        
        if len(todas_edades) == 0:
            return 0
        
        promedio = sum(todas_edades) / len(todas_edades)
        return promedio
    
    def buscar_persona(self, nombre, apellido):
        for charla in self.charlas:
            if charla.speaker.nombre == nombre and charla.speaker.apellido == apellido:
                return f"encontrado como speaker en: {charla.nombre_charla}"
            
            for participante in charla.participantes:
                if participante.nombre == nombre and participante.apellido == apellido:
                    return f"encontrado como participante en: {charla.nombre_charla}"
        
        return "no encontrado"
    
    def eliminar_charlas_por_ci(self, ci):
        charlas_a_eliminar = []
        
        for charla in self.charlas:
            if charla.speaker.ci == ci:
                charlas_a_eliminar.append(charla)
        
        for charla in charlas_a_eliminar:
            self.charlas.remove(charla)
            self.nc -= 1
        
        return len(charlas_a_eliminar)
    
    def ordenar_charlas_por_participantes(self):
        self.charlas.sort(key=lambda charla: charla.np, reverse=True)
    
    def mostrar_charlas(self):
        print(f"\n--- charlas del evento: {self.nombre} ---")
        for i, charla in enumerate(self.charlas, 1):
            print(f"{i}. {charla.nombre_charla} - {charla.lugar}")
            print(f"   speaker: {charla.speaker.nombre} {charla.speaker.apellido}")
            print(f"   participantes: {charla.np}")


print("speakers...")
speaker1 = Speaker("juan carlos", "mendoza", 35, "1234567", "tecnologia")
speaker2 = Speaker("ana maria", "torres", 28, "7654321", "ciencias")
speaker3 = Speaker("luis alberto", "garcia", 40, "1111111", "educacion")

print("participantes...")
part1 = Persona("carlos", "perez", 20, "2222222")
part2 = Persona("maria elena", "lopez", 22, "3333333")
part3 = Persona("jorge", "gomez", 25, "4444444")
part4 = Persona("sofia", "martinez", 19, "5555555")
part5 = Persona("diego", "silva", 30, "6666666")
part6 = Persona("patricia", "rojas", 24, "7777777")
part7 = Persona("roberto", "vargas", 27, "8888888")

# crear cha
charla1 = Charla("auditorio principal", "i a", speaker1)
charla2 = Charla("sala 1", "robotica", speaker2)
charla3 = Charla("sala 2", "metodo ensenanza", speaker3)

# agregar participantes a las charlas
charla1.agregar_participante(part1)
charla1.agregar_participante(part2)
charla1.agregar_participante(part3)
charla1.agregar_participante(part6)

charla2.agregar_participante(part2)
charla2.agregar_participante(part4)
charla2.agregar_participante(part7)

charla3.agregar_participante(part1)
charla3.agregar_participante(part3)
charla3.agregar_participante(part5)

# crea
evento = Evento("congreso de tecnologia 2024")

# agr
evento.agregar_charla(charla1)
evento.agregar_charla(charla2)
evento.agregar_charla(charla3)


evento.mostrar_charlas()

#a)
print(f"\n--- edad promedio de participantes ---")

promedio = evento.edad_promedio_participantes()
print(f"edad promedio: {promedio:.1f} años")

#b)
print(f"\n--- buscar persona ---")

resultado1 = evento.buscar_persona("carlos", "perez")
print(f"carlos perez: {resultado1}")

resultado2 = evento.buscar_persona("juan carlos", "mendoza")

print(f"juan carlos mendoza: {resultado2}")

resultado3 = evento.buscar_persona("pedro", "castro")
print(f"pedro castro: {resultado3}")


#c) 
print(f"\n--- eliminar charlas por ci ---")
eliminadas = evento.eliminar_charlas_por_ci("7654321")

print(f"charlas eliminadas: {eliminadas}")



evento.mostrar_charlas()

#d)
print(f"\n--- ordenar charlas por participantes ---")
evento.ordenar_charlas_por_participantes()
evento.mostrar_charlas()