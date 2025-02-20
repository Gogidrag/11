import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

def main():

    print("Добро пожаловать, вот доступные задачи:")
    tasks = [
        "distance",
        "circle",
        "operations",  
        "favorite_movies",
        "my_family",
        "zoo",
        "song_list",
        "secret",
        "garden",
        "shopping",
        "store"
    ]

    for i, task in enumerate(tasks,start=1):
        print(f"{i},{task}")

    try:
        choise = int(input("Выберите номер задачи (1-11):"))
        if choise < 1 or choise > len(tasks):
            print("Неверный номер задачи,Выберите число от 1 до 11")
            return
        
        filenames = [
           "distance",
            "circle",
            "operations",  
            "favorite_movies",
            "my_family",
            "zoo",
            "song_list",
            "secret",
            "garden",
            "shopping",
            "store"
        ]

        selected_module = filenames[choise - 1]
        print(f"Запуск задачи:{tasks[choise - 1]}")
        exec(f"import {selected_module}")
    except ValueError:
        print(f"Введите корректный номер задачи(число)")
    except ModuleNotFoundError:
        print("Не удалось найти указанную задачу, проверьте название файла")
if __name__ == "__main__":
    main()