animation = input()

animations = {
    "Pokemon": "Pikachu",
    "Digimon": "Agumon",
    "Yugioh": "Black Magician"
}

print(animations.get(animation, "I don`t know"))