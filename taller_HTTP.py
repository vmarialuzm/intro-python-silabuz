import requests

url = "https://pokeapi.co/api/v2/pokemon/"


def get_pokemon(pokemon):
    response = requests.get(url+pokemon)
    if response.status_code==200:
        response_json=response.json()
        name_pokemon=response_json["name"]
        peso_pokemon=response_json["weight"]
        lista_habilidades=[habilidad["ability"]["name"] for habilidad in response_json["abilities"]]
        dicc_estadisticas={ estadistica["stat"]["name"]:estadistica["base_stat"] for estadistica in response_json["stats"]}

        print("Nombre: ",name_pokemon)
        print("Peso: ",peso_pokemon)
        print("Lista de habilidades: ",lista_habilidades)
        print("Diccionario de estadisticas: ",dicc_estadisticas)


lista_pokemones=["bulbasaur", "squirtle", "charmander", "abra"]
for pokemon in lista_pokemones:
    get_pokemon(pokemon)
    print("*"*20)







    

