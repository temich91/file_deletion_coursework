import os
import random


# Функция удаления файла алгоритмом DoD 5220.22-M
def remove_file(file_path):
    file_len = os.path.getsize(file_path)
    with open(file_path, "wb") as file:
        file.write(b"0" * file_len)
        file.write(b"1" * file_len)
        file.write(random.randbytes(file_len))
    os.remove(file_path)


# Функция рекурсивного удаления папки
def remove_dir(dir_path):
    files = os.listdir(dir_path)
    for file in files:
        file_path = f"{dir_path}\\{file}"
        if os.path.isdir(file_path):
            remove_dir(file_path)
        else:
            remove_file(file_path)
    os.rmdir(dir_path)


# Основная функция
def main():
    while True:
        path = input("Введите путь файла/папки для удаления (q для выхода):")
        if path == "q":
            print("Завершение программы.")
            return
        # Проверка существования объекта по заданному пути
        if not os.path.exists(path):
            print(f"Файла/папки по пути {path} не существует.")
            continue

        # Подтверждение удаления
        acception = ''
        while acception not in ["yes", "no"]:
            acception = input(f'Подтвердите удаление папки по пути {path} (yes/no)').lower()

        if acception == "no":
            continue
        elif acception == "yes":
            # Если по заданному пути расположена папка, вызывается функция удаления папки
            if os.path.isdir(path):
                try:
                    remove_dir(path)
                # Обработка ошибки - вывод сообщения
                except Exception as e:
                    print(e)
                    print(f"Удаление по пути {path} невозможно")
                    continue
                print("Папка удалена.")

            # Если по заданному пути расположен файл, вызывается функция удаления файла
            elif os.path.isfile(path):
                try:
                    remove_file(path)
                # Обработка ошибки - вывод сообщения
                except:
                    print(f"Удаление по пути {path} невозможно")
                    continue
                print("Файл удален.")
            # Если объект не распознан, удаление невозможно
            else:
                print(f"Файла/папки по пути {path} не существует.")
                continue

# Запуск основной функции
if __name__ == "__main__":
    main()
