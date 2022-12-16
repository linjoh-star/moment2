
sekunder = int(input("Ange antalet sekunder: "))


timmar = sekunder // 3600
minuter = (sekunder % 3600) // 60


print(f"Inmatning: {sekunder} -> {timmar}h{minuter}m{sekunder % 60}s")
