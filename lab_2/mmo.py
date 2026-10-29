# Створити гру, яка дозволяє визначити від користувача дію з набору доступних та виконати її 
import random

random_number = random.choice(range(10, 101, 10))
user_number = 50
name = input("Введіть ваше ім'я: ")
print(f"Привіт, {name}! Гра - вгадай число від 10 до 100, яке я загадав. Ти починаєш з: {user_number}")

action_statistics = {
    "w": 0,
    "s": 0,
    "0": 0
}

user_actions = {
    "w": "Збільшити вгадуване число",
    "s": "Зменшити вгадуване число",
    "0": "Вийти з гри"
}

print("Вітаємо у грі! Ось доступні дії:")
for key, value in user_actions.items():
    print(f"|{key} - {value} \t|")

while True:
    action = input(f"{name}, твій вибір: ")
    print(f"Ви обрали дію: {user_actions.get(action, 'Невідома дія')}")
    action_statistics[action] = action_statistics.get(action, 0) + 1
    if action == "0":
        print("Вихід з гри...")
        break

    if action == "w":
        user_number += 10
        print(f"Ваше число збільшено до: {user_number}")
    elif action == "s":
        user_number -= 10
        print(f"Ваше число зменшено до: {user_number}")

    if user_number > random_number:
        print("Ваше число більше за загаданого. Спробуйте ще раз.")
    elif user_number < random_number:
        print("Ваше число менше за загаданого. Спробуйте ще раз.")
    else:
        print(f"Вітаємо {name}! Ви вгадали число!")
        break

print("Статистика дій:")
for key, value in action_statistics.items():
    print(f"{key} була виконана {value} разів.")
