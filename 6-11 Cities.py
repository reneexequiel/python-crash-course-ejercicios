

cities = {

    "puerto varas":{
        "Pais":"Chile",
        "Region":"Los lagos",
        "Poblacion":44578,
        "Gentilicio":"Portovarino",
    },

    "Frutillar":{
        "Pais":"Chile",
        "Region":"Los lagos",
        "Poblacion":18428,
        "Gentilicio":"Frutillarino",
    },

    "arequipa":{
        "Pais":"Peru",
        "Region":"Arequipa",
        "Poblacion":1157500,
        "Gentilicio":"Arequipeño",
    }

}

for ciudades, info in cities.items():
    print(ciudades.title(), "se encuentra en: ", info["Pais"].title(),".")
    print("-"," Tiene una poblacion de: ",info["Poblacion"],".")
    print("-"," Se encuentra en la region de: ",info["Region"],".")
    print("-"," Su gentilicio es: ",info["Gentilicio"].title(),"\n")
        
    