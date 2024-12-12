import os
import random


def remove_file(file_path):
    file_len = os.path.getsize(file_path)
    with open(file_path, "wb") as file:
        file.write(b"0" * file_len)
        file.write(b"1" * file_len)
        file.write(random.randbytes(file_len))
    os.remove(file_path)


def remove_dir(dir_path):
    files = os.listdir(dir_path)
    for file in files:
        file_path = f"{dir_path}\\{file}"
        if os.path.isdir(file_path):
            remove_dir(file_path)
        else:
            remove_file(file_path)
    os.rmdir(dir_path)


def main():
    while True:
        path = input("Введите путь файла/папки для удаления (q для выхода):")
        if path == "q":
            print("Завершение программы.")
            return
        if not os.path.exists(path):
            print(f"Файла/папки по пути {path} не существует.")
            continue

        acception = ''
        while acception not in ["yes", "no"]:
            acception = input(f'Подтвердите удаление папки по пути {path} (yes/no)').lower()

        if acception == "no":
            continue
        elif acception == "yes":
            if os.path.isdir(path):
                try:
                    remove_dir(path)
                except Exception as e:
                    print(e)
                    print(f"Удаление по пути {path} невозможно")
                    continue
                print("Папка удалена.")
            elif os.path.isfile(path):
                try:
                    remove_file(path)
                except:
                    print(f"Удаление по пути {path} невозможно")
                    continue
                print("Файл удален.")
            else:
                print(f"Файла/папки по пути {path} не существует.")
                continue


if __name__ == "__main__":
    main()
