import json

tasks = []
try:
    with open ('tasks.json', 'r', encoding='utf-8') as file:
        tasks = json.load(file)    
except (FileNotFoundError, json.JSONDecodeError):
    tasks = []
    print('Файл с задачами не найден или может быть пустым или поврежденным.' \
    ' Создан пустой список.')

def save_tasks():
    with open('tasks.json', 'w', encoding='utf-8') as file:
        json.dump(tasks, file)

def show_task():
    if len(tasks) == 0:
        print('Список задач пуст')
    else:
        for index, item in enumerate(tasks, start=1):
            if item['completed'] == True:
                print(f"{index}){item['name']} - 'Выполнена'")
            else:
                print(f"{index}) {item['name']} - 'Не выполнена'")

def del_task():
    if len(tasks) == 0:
        print('Нет задач для удаления')
    else:
        while True:
            try:
                del_task = int(input('Какую задачу удалить? '))
                break
            except ValueError:
                print('Напишите номер задачи')
        if del_task > len(tasks) or del_task < 1:
            print('Ошибка')
        else:
            tasks.pop(del_task - 1)
            for i in tasks:
                print(i['name'])
    save_tasks()

def add_task():
    while True:
        new_task = input('Введите новую задачу: ').strip()
        if new_task == "":
            print('Название задачи не может быть пустым')
        else:
            tasks.append({'name' : new_task,
                        'completed' : False
            })
            print('Ваша задача успешно добавлена')
            for index, item in enumerate(tasks, start=1):
                if item['completed'] == True:
                    print(f"{index}) {item['name']} - 'Выполнена'")
                else:
                    print(f"{index}) {item['name']} - 'Не выполнена'")
            break
    save_tasks()


def mark_task():
    if len(tasks) == 0:
        print('Нет задач для отметки')
    else:
        while True:
            try:
                question = int(input('Какую задачу отметить выполненной? '))
                break
            except ValueError:
                print('Напишите число')
        if question > len(tasks) or question < 1:
            print('Ошибка')
        else:
            tasks[question - 1]['completed'] = True
            for task in tasks:
                if task['completed'] == False:
                    print(f"{task['name']} - Не выполнена")
                else:
                    print(f"{task['name']} - Выполнена")
    save_tasks()

def unmark_task():
    if len(tasks) == 0:
        print('Нет задач для изменения статуса')
    else:
        while True:
            try:
                question = int(input('Какую задачу отметить невыполненной? '))
                break
            except ValueError:
                print('Напишите число')
        if question > len(tasks) or question < 1:
            print('Ошибка')
        else:
            tasks[question - 1]['completed'] = False
            for task in tasks:
                if task['completed'] == False:
                    print(f"{task['name']} - Не выполнена")
                else:
                    print(f"{task['name']} - Выполнена")
    save_tasks()



while True:
    print('1. Показать задачу')
    print('2. Добавить задачу')
    print('3. Удалить задачу')
    print('4. Отметить задачу выполненной')
    print('5. Отметить задачу невыполненной')
    print('6. Выйти')

    choice = input('Выберите действие: ')
    if choice == '6':
        break

    elif choice == '1':
        show_task()

    elif choice == '2':
        add_task()

    elif choice == '3':
        del_task()

    elif choice == '4':
        mark_task()

    elif choice == '5':
        unmark_task()

# Эта программа поможет хранить ваши любимые игры

