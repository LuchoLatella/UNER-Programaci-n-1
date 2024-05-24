#Pertenencia
tortugas = ["Leonardo", "Raphael", "Donatello", "Miguel Ángel"]
i = 0
while i < len(tortugas):
    print(tortugas[i])
    i = i + 1
    
print('"Leonardo" in tortugas?', "Leonardo" in tortugas)
print('"leonardo" in tortugas?', "leonardo" in tortugas)
print('"Rocoso" in tortugas?', "Rocoso" in tortugas)
print('"Miguel Ángel" in tortugas?', "Miguel Ángel" in tortugas)
print('"Beboop" not in tortugas?', "Bebop" not in tortugas)