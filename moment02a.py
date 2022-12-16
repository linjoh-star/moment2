# Fråga användaren om radien
radius = float(input("Ange radien för cirkeln: "))

# Använd närmevärdet 3,14 för pi
pi = 3.14

# Beräkna area och omkrets
area = pi * radius**2
omkrets = 2 * pi * radius

# Skriv ut resultaten med två decimaler
print(f"Radie: {radius:.2f}")
print(f"Area: {area:.2f}")
print(f"Omkrets: {omkrets:.2f}")
