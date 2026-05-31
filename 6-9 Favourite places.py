

favourite_places = {
    "rene":["puerto varas", "frutillar", "santa cruz"],
    "pamela":["puerto varas", "lima"],
    "mama":["serena", "lima", "tacna"]
}

for nombre, lugares in favourite_places.items():
    print(nombre.title() + " Prefiere los siguientes lugares para vacacionar:")
    for lugar in lugares:
        print("-", lugar.title())