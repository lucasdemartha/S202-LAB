from db.pokedex import Pokedex
from helper.WriteAJson import writeAJson

pokedex = Pokedex()
'''
5
pokemons = pokedex.egg("Dratini")
print(pokemons)
'''

'''
4
pokemons = pokedex.Legendary()
print(pokemons)
'''

'''
3
pokemons = pokedex.CandyEvolution("Pikachu")
print(pokemons)
'''

'''
2
pokemons = pokedex.getFirstGym()
print(pokemons)
'''


'''
1
pokemons = pokedex.getAshInitial()
print(pokemons)
'''

'''
Example
pokemons = pokedex.getPokemonByName("Bulbasaur")

print(pokemons)
writeAJson(pokemons,"Bulbasaur")
'''


