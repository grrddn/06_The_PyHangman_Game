import random

word_list = ["Aguacate", "Mariposa", "Platano"]
adivinanzas = ["Agua pasa por mi casa, cate de mi corazón", "Antes huevecito, después capullito y más tarde volaré como un pajarito. ¿Sabes quién soy?", "Oro parece, plata no es. Abran las cortinas y verán lo que es."]
stages = ["⏩⏩⏩⏩⏩❌", "⏩⏩⏩⏩⏩ ❌", "⏩⏩⏩⏩  ❌", "⏩⏩⏩   ❌",  "⏩⏩    ❌", "⏩    ❌"]

chosen_word = random.choice(word_list)

if chosen_word == "Aguacate":
    adivinanza = adivinanzas[0]
elif chosen_word == "Mariposa":
    adivinanza = adivinanzas[1]
elif chosen_word == "Platano":
    adivinanza = adivinanzas[2]

print('''

      ¡¡¡¡BIENVENIDO AL JUEGO DE LA ADIVINANZA!!!!!
            ¿Puedes adivinar la palabra?
            ¡¡¡Que comience el juego!!!

''')

print(f"La adivinanza es: {adivinanza} \n")
print(f'Una palabra de {len(palabra)} letras\n')

chosen_word = chosen_word.upper()

for i in range(len(chosen_word)):
    print("_", end=" ")

game_over = False
correct_letters = []
lives = 6

while not game_over:
    guess = input("\nAdivina una letra: \n").upper()
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += guess
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            game_over = True
            print("¡Perdiste! \nLa palabra era:", chosen_word)

    print(display)

    if "_" not in display:
        game_over = True
        print("¡Ganaste! \nLa palabra era:", chosen_word)