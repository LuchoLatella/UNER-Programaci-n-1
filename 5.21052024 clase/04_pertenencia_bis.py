#Pertenencia
def buscar_sin_in(tortugas, busqueda):
    for t in tortugas:
        if t == busqueda:
            return True
    return False

tortugas = ["Leonardo", "Raphael", "Donatello", "Miguel Ángel"]
i = 0
while i < len(tortugas):
    print(tortugas[i])
    i = i + 1

print("Está splinter:", buscar_sin_in(tortugas, 'Splinter'))

print("Está Donatello:", buscar_sin_in(tortugas, 'Donatello'))