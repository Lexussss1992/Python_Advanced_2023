import pokemon

class Trainer:
    def __init__(self, name):
        self.pokemons = []
        self.name = name

    def add_pokemon(self, pokemon):
        self.pokemons.append(pokemon)
        return f'Caught {pokemon.pokemon_details()}'


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())