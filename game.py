import json
import random
import os

user_name = None
this_stage = None


def star_menu(user_name, this_stage):
    while True:

        menu_items = ('Новая игра', 'Продолжить игру', 'Удалить сохранение', 'Выход из игры')
        for i, item in enumerate(menu_items):
            print(f'{i + 1}. {item}')
        try:
            choice = int(input('Выберете действие: '))
            match choice:
                case 1:
                    print('-------------------')
                    new_save(user_name, this_stage)
                case 2:
                    print('-------------------')
                    load_save(user_name, this_stage)
                case 3:
                    print('-------------------')
                    delete_save()
                case 4:
                    print('-------------------')
                    breakpoint()
        except:
            print('-------------------')
            star_menu(user_name, this_stage)


def new_save(user_name, this_stage):
    print('Прежде, чем начать игру, вы должны определиться с выбором вашего героя. Как вас зовут?')
    user_name = str(input('Введите свое имя: '))
    this_stage = "choose_character"
    save(user_name, this_stage)
    game_start(user_name, this_stage)
    return user_name


def save(user_name, this_stage):
    save_data = {
        "name": user_name,
        "stage": this_stage
    }
    with open('save_data.json', 'w', encoding='utf-8') as file:
        return json.dump(save_data, file, indent=2)


def load_save(user_name, this_stage):
    if os.path.exists('save_data.json'):
        with open('save_data.json') as file:
            save_data = json.load(file)
            this_stage = save_data["stage"]
            if this_stage == "game_start":
                game_start(user_name, this_stage)
            elif this_stage == "choose_character":
                choose_character(user_name, this_stage)
            elif this_stage == "game_loop":
                game_loop(user_name, this_stage)
            elif this_stage == "game":
                game(user_name, this_stage)
            elif this_stage == "talk":
                talk(user_name, this_stage)
            elif this_stage == "dialog":
                dialog(user_name, this_stage)
            elif this_stage == "continue_path":
                continue_path(user_name, this_stage)
            elif this_stage == "continue_path_2":
                continue_path_2(user_name, this_stage)
            elif this_stage == "go_inside":
                go_inside(user_name, this_stage)
            elif this_stage == "chimney":
                chimney(user_name, this_stage)
            elif this_stage == "chest":
                chest(user_name, this_stage)
            elif this_stage == "fight_1":
                fight_1(user_name, this_stage)
            elif this_stage == "fight_2":
                fight_2(user_name, this_stage)
            elif this_stage == "final_1":
                final_1(user_name, this_stage)
            elif this_stage == "final_2":
                final_2(user_name, this_stage)
            elif this_stage == "final_3":
                final_3(user_name, this_stage)
            else:
                return {}


def delete_save():
    if os.path.exists('save_data.json'):
        os.remove('save_data.json')
        print("Удаление сохранения успешно!")
    else:
        print("Сохранение не найдено!")


def game_start(user_name, this_stage):
    while True:
        try:
            choice = input('Начать игру? (Да/Нет): ').lower()
            match choice:
                case 'да':
                    print('-------------------')
                    choose_character(user_name, this_stage)
                case 'нет':
                    print('-------------------')
                    star_menu(user_name, this_stage)
                case _:
                    print('-------------------')
                    game_start(user_name, this_stage)
        except:
            print('-------------------')
            print("Введите 'Да' или 'Нет'.")
            print('-------------------')
            break


def choose_character(user_name, this_stage):
    while True:
        characters = ['Маг', 'Асассин', 'Лучник', 'Варвар']
        descriptions = {'Маг': 'Вы владеете различными заклинаниями.',
                        'Асассин': 'Вы достаточно ловки, чтобы избежать атак врага и нанести точечный удар.',
                        'Лучник': 'Меткая стрелба - ваш конёк! Издалека вы куда опаснее для врагов.',
                        'Варвар': 'Только грубая сила и топор. Решайте все проблемы самым простым способом.'}
        for i, character in enumerate(characters):
            print(f'{i + 1}. {character}')
        try:
            choice_characters = int(input('Выберете класс своего персонажа: '))
            character = characters[int(choice_characters) - 1]
            print(f'Вы {character.lower()} по имени {user_name}.')
            print(f'{descriptions[character]}')
            this_stage = "choose_character"
            save(user_name, this_stage)
            game_loop(user_name, this_stage)
        except ValueError:
            print('Вы не выбрали персонажа.')
            print('Вы не выбрали персонажа. Попробуйте снова.')
            choose_character(user_name, this_stage)


def game_loop(user_name, this_stage):
    while True:
        print('Находясь в городе вы понимаете, что жизнь здесь скучная и рутинная. Вы решаете отправиться в новое '
              'приключение, дабы найти сокровище или раздобыть немного денег.')
        choice = input('Вы согласный отправиться в путь? (Да/Нет): ').lower()
        if choice == 'да':
            print('Удачи в приключении!')
            this_stage = "game_loop"
            save(user_name, this_stage)
            game(user_name, this_stage)
            break
        elif choice == 'нет':
            print('До свидания.')
            breakpoint()
            break
        else:
            print("Введите 'Да' или 'Нет'.")


def game(user_name, this_stage):
    this_stage = "game"
    save(user_name, this_stage)
    try:
        print(
            'В очередном своём приключении вы заблудились в глубоком темном лесу... посреди чащи в ночи стоит странный незнакомец в темно-сером потрёпанном плаще.')
        actions = {'1': 'Поговорить', '2': 'Попробовать сразиться', '3': 'Пройти мимо не обращая внимания'}
        while True:
            print('Что вы хотите сделать?')
            for key, value in actions.items():
                print(f'{key}. {value}')
            choice = input('Введите номер действия: ')
            match choice:
                case '1':
                    print('Вы выбрали действие \'Поговорить\'.')
                    this_stage = "talk"
                    save(user_name, this_stage)
                    talk(user_name, this_stage)
                    break
                case '2':
                    print('Вы выбрали действие \'Попробовать сразиться\'.')
                    this_stage = "fight_1"
                    save(user_name, this_stage)
                    fight_1(user_name, this_stage)
                    break
                case '3':
                    print('Вы выбрали действие \'Пройти мимо не обращая внимания\'.')
                    this_stage = "continue_path"
                    save(user_name, this_stage)
                    continue_path(user_name, this_stage)
                    break
                case _:
                    print('Неверный выбор. Попробуйте еще раз.')
                    break
    except:
        print('Попробуйте снова.')
        game(user_name, this_stage)


def talk(user_name, this_stage):
    name_n = 'Авгур'
    print(
        f'Заговорив с подозрительным незнакомцем, выяснилось, что на самом деле вы говорите с могущественным некромантом по имени {name_n}.')
    print('Так просто вы уже не уйдёте, вам стоит рещить, что делать дальше.')
    actions = {'1': 'Попробовать договориться', '2': 'Попробовать сразиться'}
    while True:
        print('Что вы хотите сделать?')
        for key, value in actions.items():
            print(f'{key}. {value}')
        try:
            choice = input('Введите номер действия: ')
            match choice:
                case '1':
                    print('Вы выбрали действие \'Попробовать договориться\'.')
                    this_stage = "dialog"
                    save(user_name, this_stage)
                    dialog(user_name, this_stage)
                    break
                case '2':
                    print('Вы выбрали действие \'Попробовать сразиться\'.')
                    this_stage = "fight_1"
                    save(user_name, this_stage)
                    fight_1(user_name, this_stage)
                    break
        except:
            print('Попробуйте снова.')
            this_stage = "talk"
            save(user_name, this_stage)
            talk(user_name, this_stage)
            break


def dialog(user_name, this_stage):
    name_n = 'Авгур'
    dialog_res = random.randint(1, 20)
    if dialog_res <= 10:
        print(
            'Благодаря вашему участию в гильдии и невероятному красноречию удалось убедить злого некроманта \'Авгура\' отпустить вас.')
        this_stage = "continue_path"
        save(user_name, this_stage)
        continue_path(user_name, this_stage)
    else:
        print(
            'Не смототря на ваши превосходные умения убеждения и навыки красноречия вам не удалось убедить некроманта. Ваши попытки убеждения лишь рассмешили \'Авгура\'.')
        print(f'Почувствовав вашу нечтожность, {name_n} решает убить вас. Придется защищаться.')
        this_stage = "fight_1"
        save(user_name, this_stage)
        fight_1(user_name, this_stage)


def continue_path(user_name, this_stage):
    try:
        print('Вы решили продолжить свой путь. На вашем пути вы видите диких животных, как бы вы поступили?')
        actions = {'1': 'Попробовать сразиться', '2': 'Пройти мимо не обращая внимания'}
        while True:
            print('Что вы хотите сделать?')
            for key, value in actions.items():
                print(f'{key}. {value}')
            choice = input('Введите номер действия: ')
            match choice:
                case '1':
                    print('Вы выбрали действие \'Попробовать сразиться\'.')
                    print('Собравшись с мыслями вы принимаете решение сразиться с ними.')
                    this_stage = "fight_2"
                    save(user_name, this_stage)
                    fight_2(user_name, this_stage)
                    break
                case '2':
                    print('Вы выбрали действие \'Пройти мимо не обращая внимания\'.')
                    print('Вы встречаете диких животных, сумев их обойти вы продолжаете свой путь.')
                    this_stage = "continue_path_2"
                    save(user_name, this_stage)
                    continue_path_2(user_name, this_stage)
                    break
    except:
        print('Попробуйте снова.')
        this_stage = "continue_path"
        save(user_name, this_stage)
        continue_path(user_name, this_stage)


def continue_path_2(user_name, this_stage):
    try:
        print('Вы натыкаетесь на старую хижину.')
        actions = {'1': 'Зайти в хижину', '2': 'Продолжить свой путь'}
        while True:
            print('Что вы хотите сделать?')
            for key, value in actions.items():
                print(f'{key}. {value}')
            choice = input('Введите номер действия: ')
            match choice:
                case '1':
                    print('Вы выбрали действие \'Зайти в хижину\'.')
                    this_stage = "go_inside"
                    save(user_name, this_stage)
                    go_inside(user_name, this_stage)
                    break
                case '2':
                    print('Вы выбрали действие \'Продолжить свой путь\'.')
                    this_stage = "final_1"
                    save(user_name, this_stage)
                    final_1(user_name, this_stage)
                    break
    except:
        print('Попробуйте снова')
        this_stage = "continue_path_2"
        save(user_name, this_stage)
        continue_path_2(user_name, this_stage)


def go_inside(user_name, this_stage):
    try:
        print('Вы заходите внутрь старой заброшенной хижины. Вы видите обгоревший домоход и сундук рядон с ним.')
        actions = {'1': 'Исследовать дымоход', '2': 'Заглянуть внутрь сундука',
                   '3': 'Ничего не сделать и продолжить свой путь'}
        while True:
            print('Что вы сделаете?')
            for key, value in actions.items():
                print(f'{key}. {value}')
            choice = input('Введите номер действия: ')
            match choice:
                case '1':
                    print('Вы выбрали действие \'Исследовать дымоход\'.')
                    this_stage = "chimney"
                    save(user_name, this_stage)
                    chimney(user_name, this_stage)
                    break
                case '2':
                    print('Вы выбрали действие \'Заглянуть внутрь сундука\'.')
                    this_stage = "chest"
                    save(user_name, this_stage)
                    chest(user_name, this_stage)
                    break
                case '3':
                    print('Вы выбрали действие \'Ничего не сделать и продолжить свой путь\'.')
                    print('Ничего не найдя внутри вы возвращаетесь на большую дорогу.')
                    this_stage = "final_1"
                    save(user_name, this_stage)
                    final_1(user_name, this_stage)
                    break
    except:
        print('Попробуйте снова')
        this_stage = "go_inside"
        save(user_name, this_stage)
        go_inside(user_name, this_stage)


def chimney(user_name, this_stage):
    win = random.randint(1, 18)
    if win == 2:
        print('В дымоходе вы нахолите небольшой свёрток, внутри которого лежит кусочек золота.')
        this_stage = "final_3"
        save(user_name, this_stage)
        final_3(user_name, this_stage)
    else:
        print('Ничего не найдя внутри вы возвращаетесь на большую дорогу.')
        this_stage = "final_1"
        save(user_name, this_stage)
        final_1(user_name, this_stage)


def chest(user_name, this_stage):
    win = random.randint(1, 6)
    if win == 2:
        print('Внутри непреметного старого сундучка вы находите сокровища, которые и искали.')
        this_stage = "final_3"
        save(user_name, this_stage)
        final_3(user_name, this_stage)
    else:
        print('Ничего не найдя внутри вы возвращаетесь на большую дорогу.')
        this_stage = "final_1"
        save(user_name, this_stage)
        final_1(user_name, this_stage)


def fight_1(user_name, this_stage):
    print('Собравшись с мыслями вы принимаете решение вступить в бой с могущественным неркомантом \'Авгуром\'.')
    win = random.randint(1, 15)
    if win // 5 or 3 == 0:
        print('Вы отважно сражались с \'Авгуром\' и в итоге победили!')
        this_stage = "continue_path"
        save(user_name, this_stage)
        continue_path(user_name, this_stage)
    else:
        this_stage = "final_2"
        save(user_name, this_stage)
        final_2(user_name, this_stage)


def fight_2(user_name, this_stage):
    win = random.randint(2, 12)
    if win == 2 or 4 or 6:
        print('Вы отважно сражались и в итоге одержали победу!')
        this_stage = "continue_path_2"
        save(user_name, this_stage)
        continue_path_2(user_name, this_stage)
    else:
        this_stage = "final_2"
        save(user_name, this_stage)
        final_2(user_name, this_stage)


def final_1(user_name, this_stage):
    print('В конце концов, вы смогли добраться до ближайшей таверны, в которой вы и планиуете переночевать.')
    print(
        'Добравшись до ближайшей таверны вы засыпаете в комнате. Ваше приключение завершино и вы можете начать его снова.')
    game_start(user_name, this_stage)


def final_2(user_name, this_stage):
    print(
        'Потеряв все силы вы теряете сознание и погибаете. Это был ваш последний бой, на данном моменте ваши приключения заканчиваются. Конец игры.')
    print('Ваше приключение завершино и вы можете начать его снова.')
    game_start(user_name, this_stage)


def final_3(user_name, this_stage):
    print('Вместе со своим сокровищем вы смогли добраться до ближайшей таверны, в которой вы и планиуете переночевать.')
    print('Вы победили!')
    print('Ваше приключение завершино и вы можете начать его снова.')
    game_start(user_name, this_stage)


star_menu(user_name, this_stage)
