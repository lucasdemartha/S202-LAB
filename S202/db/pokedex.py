from db.database import Database


class Pokedex:
    def __init__(self):
        self.db = Database(database="pokedex", collection="pokemons")
        self.db.resetDatabase()
        self.collection = self.db.collection

    def find(self, filters: dict):
        response = self.collection.find(filters)
        pokemons = []
        for pokemon in response:
            pokemons.append(pokemon)
        return pokemons

    def getAllPokemons(self):
        response = self.collection.find({}, {"name": 1, "_id": 0})
        pokemons = []
        for pokemon in response:
            pokemons.append(pokemon)
        return pokemons

    def getPokemonByName(self, name: str):
        response = self.collection.find({"name": name},
                                        {"_id": 0, "name": 1,
                                         "next_evolution": 1, "prev_evolution": 1,
                                         "type": 1, "weaknesses": 1})
        result = {}
        for pokemon in response:
            result = pokemon
        return result

    def getPokemonsByType(self, type: list):
        response = self.collection.find({"type": {"$all": type}}, {
            "_id": 0, "name": 1, "type": 1})
        result = []
        for pokemon in response:
            result.append(pokemon)
        return result

    def getPokemonEvolutionsByName(self, name: str):
        pokemon = self.getPokemonByName(name)

        evolutions = [pokemon['name']]
        hasNextEvolutions = ('next_evolution' in pokemon)
        hasPrevEvolutions = ('prev_evolution' in pokemon)

        if hasNextEvolutions:
            nextEvolutions = list(pokemon['next_evolution'])
            for evolution in nextEvolutions:
                evolution = self.getPokemonByName(evolution['name'])
                evolutions.append(evolution['name'])

        if hasPrevEvolutions:
            previousEvolutions = list(pokemon['prev_evolution'])
            for evolution in previousEvolutions:
                evolution = self.getPokemonByName(evolution['name'])
                evolutions.append(evolution['name'])

        return evolutions

    def getAshInitial(self):
        response = self.collection.find({"name": "Pikachu"},
                                        {"_id": 0, "name": 1,
                                         "next_evolution": 1, "prev_evolution": 1,
                                         "type": 1, "weaknesses": 1})
        result = {}
        for pokemon in response:
            result = pokemon
        return result

    def getFirstGym(self):
        print("Welcome to Brock's Gym")
        response = self.collection.find({"name": "Geodude"},
                                        {"_id": 0, "name": 1,
                                         "type": 1, "weaknesses": 1})
        poke1 = {}
        for pokemon in response:
            poke1 = pokemon
        responses = self.collection.find({"name": "Onix"},
                                        {"_id": 0, "name": 1,
                                         "type": 1, "weaknesses": 1})
        poke2 = {}
        for pokemons in responses:
            poke2 = pokemons
        return poke1, poke2

    def CandyEvolution(self, name: str):
        response = self.collection.find({"name": name},
                                        {"_id": 0, "name": 1,"candy_count": 1,})
        result = {}
        for pokemon in response:
            result = pokemon
        return result

    def Legendary(self):
        response = self.collection.find({"name": "Articuno"},
                                        {"_id": 0, "name": 1,
                                         "type": 1})
        art = {}
        for pokemon in response:
            art = pokemon

        response = self.collection.find({"name": "Zapdos"},
                                        {"_id": 0, "name": 1,
                                         "type": 1})
        zap = {}
        for pokemon in response:
            zap = pokemon

        response = self.collection.find({"name": "Moltres"},
                                        {"_id": 0, "name": 1,
                                         "type": 1})
        mol = {}
        for pokemon in response:
            mol = pokemon

        response = self.collection.find({"name": "Mewtwo"},
                                        {"_id": 0, "name": 1,
                                         "type": 1})
        mt = {}
        for pokemon in response:
            mt = pokemon

        response = self.collection.find({"name": "Mew"},
                                        {"_id": 0, "name": 1,
                                         "type": 1})
        mew = {}
        for pokemon in response:
            mew = pokemon
        
        return art, zap, mol, mt, mew

    def egg(self, name: str):
        response = self.collection.find({"name": name},
                                        {"_id": 0, "name": 1,"egg": 1,})
        result = {}
        for pokemon in response:
            result = pokemon
        return result
        
