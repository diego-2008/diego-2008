class Persona:
    def __init__(self, nombre, nif, fecha_nac):
        self.nombre = nombre
        self.nif = nif
        self.fecha_nac = fecha_nac


class Jugador(Persona):
    def __init__(self, nombre, nif, fecha_nac, numFed):
        super().__init__(nombre, nif, fecha_nac)
        self.numFed = numFed

persona1 = Persona("Diego Garzon", "12345678A", "21/01/2008")
jugador1 = Jugador("Juan Garcia", "23456789B", "05/03/1985", 101)

print(f"Persona: {persona1.nombre}, NIF: {persona1.nif}, Fecha de Nacimiento: {persona1.fecha_nac}")
print(f"Jugador: {jugador1.nombre}, NIF: {jugador1.nif}, Fecha de Nacimiento: {jugador1.fecha_nac}, Numero de Federación: {jugador1.numFed}")
