import os
import shutil
import platform
import random

def create_folder():
    folder_name = input("Введите название папки: ")
    os.makedirs(folder_name, exist_ok=True)
    print(f"Папка '{folder_name}' создана.")

def delete_file_or_folder():
    name = input("Введите название файла или папки: ")
    if os.path.isdir(name):
        shutil.rmtree(name)
        print(f"Папка '{name}' удалена.")
    elif os.path.isfile(name):
        os.remove(name)
        print(f"Файл '{name}' удален.")
    else:
        print(f"'{name}' не существует.")

def copy_file_or_folder():
    source = input("Введите название файла или папки: ")
    destination = input("Введите новое название файла или папки: ")
    if os.path.isdir(source):
        shutil.copytree(source, destination)
        print(f"Папка '{source}' скопирована как '{destination}'.")
    elif os.path.isfile(source):
        shutil.copy2(source, destination)
        print(f"Файл '{source}' скопирован как '{destination}'.")
    else:
        print(f"'{source}' не существует.")

def view_directory_contents():
    contents = os.listdir()
    print("Содержимое рабочей директории:")
    for item in contents:
        print(item)

def view_folders():
    contents = [item for item in os.listdir() if os.path.isdir(item)]
    print("Папки в рабочей директории:")
    for folder in contents:
        print(folder)

def view_files():
    contents = [item for item in os.listdir() if os.path.isfile(item)]
    print("Файлы в рабочей директории:")
    for file in contents:
        print(file)

def view_os_info():
    print("Информация об операционной системе:")
    print(f"Система: {platform.system()}")
    print(f"Версия: {platform.version()}")
    print(f"Платформа: {platform.platform()}")

def creator_info():
    print("Создатель программы: Nikolas8")

def get_random_person():
    """
    Получить 1 го случайного человека
    :return:
    """
    FAMOUS_PEOPLE = {'Александр Сергеевич Пушкин': '26.06.1799', 'Михаил Юрьевич Лермонтов': '15.10.1814',
                     'Сергей Александрович Есенин': '03.10.1895', 'Владимир Семенович Высоцкий': '25.01.1938',
                     'Виктор Робертович Цой': '21.06.1962', 'Константин Эдуардович Циолковский': '17.09.1857',
                     'Сергей Павлович Королев': '12.01.1907', 'Валентин Петрович Глушко': '20.08.1908',
                     'Андрей Николаевич Туполев': '29.10.1888', 'Юрий Алексеевич Гагарин': '09.03.1934'}

    name, date = random.choice(list(FAMOUS_PEOPLE.items()))
    return name, date

def get_person_and_question():
    # Выбираем случайного человека
    name, date = get_random_person()

    # Спрашиваем когда он родился
    answer = input(f'Когда родился {name} ')

    # Если введенный год совпадает с правильным
    if answer == date:
        print('Верно')
    else:
        print(f'Неверно. Правильный ответ: {date}')

def deposit(balance):
    amount = float(input('Enter the amount to deposit: '))
    balance += amount
    print(f'Account credited with {amount}. Current balance: {balance}')
    return balance

def purchase(balance, history):
    amount = float(input('Enter the purchase amount: '))
    if amount > balance:
        print('Insufficient funds.')
    else:
        item = input('Enter the name of the purchase: ')
        balance -= amount
        history.append((item, amount))
        print(f'Purchase {item} for {amount} completed. Current balance: {balance}')
    return balance, history

def purchase_history(history):
    if not history:
        print('Purchase history is empty.')
    else:
        for item, amount in history:
            print(f'{item}: {amount}')
    return

def bank_account():
    balance = 0
    history = []

    while True:
        print('1. Deposit')
        print('2. Purchase')
        print('3. Purchase history')
        print('4. Exit')

        choice = input('Choose an option: ')
        if choice == '1':
            balance = deposit(balance)
        elif choice == '2':
            balance, history = purchase(balance, history)
        elif choice == '3':
            purchase_history(history)
        elif choice == '4':
            break
        else:
            print('Invalid option')

def change_working_directory():
    new_path = input("Введите новый путь: ")
    os.chdir(new_path)
    print(f"Рабочая директория изменена на: {os.getcwd()}")

def main():
    while True:
        print("\nМеню:")
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
            create_folder()
        elif choice == "2":
            delete_file_or_folder()
        elif choice == "3":
            copy_file_or_folder()
        elif choice == "4":
            view_directory_contents()
        elif choice == "5":
            view_folders()
        elif choice == "6":
            view_files()
        elif choice == "7":
            view_os_info()
        elif choice == "8":
            creator_info()
        elif choice == "9":
            get_person_and_question()
        elif choice == "10":
            bank_account()
        elif choice == "11":
            change_working_directory()
        elif choice == "12":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()