import random
from characters import GameCharacter

player1 = GameCharacter("Богдан", 50)
player2 = GameCharacter("Сергій", 60)
print(f"Гравці: {player1}, {player2}")

#player1.attack(int(1))
for turn in range(10):
    print(f"\n{'='*20} Хід {turn + 1} {'='*20}")
    player1_move = random.randint(0, 3)
    player2_move = random.randint(0, 3)
    if player1_move == 1:
        print(player1.attack(player2))
    elif player1_move == 2:
        print(player1.heal())
    elif player1_move == 3:
        print(player1.ulta(player2))
    else:
        print(f"{player1.name} пропускає хід.")
    if player2_move == 1:
        print(player2.attack(player1))
    elif player2_move == 2:
        print(player2.heal())
    elif player2_move == 3:
        print(player2.ulta(player1))
    else:
        print(f"{player2.name} пропускає хід.")
    print("Статуси:")
    print(player1)
    print(player2)
    print("\n")
    if player1.is_alive() and not player2.is_alive():
        print(f"{player1.name} переміг!")
        break
    elif player2.is_alive() and not player1.is_alive():
        print(f"{player2.name} переміг!")
        break
