print("Без with: помилка перериває роботу, файл залишається відкритим")
list_files = []
for i in range(5):
    # багаторазове відриття файла без закриття є проблемою, 
    # бо файл залишається відкритим і може призвести до витоку ресурсів
    list_files.append(open("test.txt", "w+", encoding="utf-8"))
    try:
        list_files[-1].write(f"{i}: Запис без контекстного менеджера\n")
    except Exception as error:
        print(f"Сталася помилка: {error}")
else:
    for f in list_files:
        f.close()
    print(f"Файли {list_files}")

print("\nЗ with: файл закривається автоматично навіть після помилки")
try:
    with open("test.txt", "a", encoding="utf-8") as f:
        f.write("Запис із контекстним менеджером\n")
        raise RuntimeError("Імітація помилки під час обробки")
except RuntimeError as error:
    print(f"Сталася помилка: {error}")

print(f"Файл закритий: {f.closed}")
