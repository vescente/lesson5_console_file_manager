def main():
    while True:
        print("1. Создать папку")
        print("2. Удалить (файл/папку)")
        print("3. Копировать (файл/папку)")
        print("4. Просмотр содержимого рабочей директории")
        print("5. Посмотреть только папки")
        print("6. Посмотреть только файлы")
        print("7. Просмотр информации об операционной системе")
        print("8. Создатель программы")
        print("9. Играть в викторину")
        print("10. Мой банковский счет")
        print("11. Смена рабочей директории")
        print("12. Выход")

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            print("1. Создать папку")
            # create_folder()
        elif choice == "2":
            print("2. Удалить (файл/папку)")
            # delete_file_or_folder()
        elif choice == "3":
            print("3. Копировать (файл/папку)")
        # copy_file_or_folder()
        elif choice == "4":
            print("4. Просмотр содержимого рабочей директории")
        # view_directory_contents()
        elif choice == "5":
            print("5. Посмотреть только папки")
        # view_folders_only()
        elif choice == "6":
            print("6. Посмотреть только файлы")
        # view_files_only()
        elif choice == "7":
            print("7. Просмотр информации об операционной системе")
        # view_os_info()
        elif choice == "8":
            print("8. Создатель программы")
        # view_creator_info()
        elif choice == "9":
            print("9. Играть в викторину")
        # play_quiz()
        elif choice == "10":
            print("10. Мой банковский счет")
        # view_bank_account()
        elif choice == "11":
            print("11. Смена рабочей директории")
        # change_working_directory()
        elif choice == "12":
            print("До свидания!")
            break
        else:
            print("Неверный пункт меню")


if __name__ == "__main__":
    main()
