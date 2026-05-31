

favourite_places = {
    "me":["puerto varas", "frutillar", "santa cruz"],
    "sister":["puerto varas", "lima"],
    "person3":["serena", "lima", "tacna"]
}

for nombre, lugares in favourite_places.items():
    print(nombre.title() + " Prefiere los siguientes lugares para vacacionar:")
    for lugar in lugares:
        print("-", lugar.title())
