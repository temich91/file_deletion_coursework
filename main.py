import os


def remove_file(file_path):
    with open(file_path, "wb") as file:
        file.write(b"")
    os.remove(file_path)


def remove_dir(dir_path):
    files = os.listdir(dir_path)
    for file in files:
        file_path = f"{dir_path}/{file}"
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
        if os.path.isdir(path):
            try:
                remove_dir(path)
            except:
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
